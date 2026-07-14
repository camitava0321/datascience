# Title: Do a Learning Python Tool with Ollama
#
# Description:
# This advanced script creates an "Auto-correcting Coding Tutor".
# 1. It asks the user for a prompt (e.g., "Write a function to add two numbers").
# 2. It asks the local LLM to generate Python code.
# 3. It tries to EXECUTE that code.
# 4. If the code fails (throws an error), it feeds the error BACK to the LLM and asks it to fix it.
# 5. It repeats this loop until the code runs successfully.
# 6. Finally, it allows the user to ask questions about specific parts of the generated code.
#
# This demonstrates a "Agentic Loop" or "Self-Correction" workflow.
#
# Installation:
# pip install streamlit ollama
#

import streamlit as st  # UI Framework
import ollama           # Local LLM interaction
import io               # For capturing output
import sys              # For stdout redirection

st.title("Ollama!")

# Input area for the user's request (e.g., "Create a list of 10 random numbers")
prompt = st.text_area(label="Write your prompt.")
button = st.button("Okay")

if button:
    if prompt:
        # --- Self-Correction Loop ---
        # We enter a 'while True' loop that will only break when valid code is generated.
        while True:
            # 1. Generate Code
            # We append a strict instruction to the prompt to ensure we get ONLY code.
            response = ollama.generate(model='tinyllama:latest', prompt=prompt + "\nNote: Output must have only Python code, do not add any other explanation.")
            
            # Print the raw response to the terminal for debugging
            print(response["response"])

            # 2. Setup Output Capture
            # Just like in 6.py, we redirect stdout to capture print statements and errors.
            old_stdout = sys.stdout
            sys.stdout = buffer = io.StringIO()

            # 3. Clean the Code
            # LLMs often wrap code in Markdown backticks (```python ... ```).
            # We remove these to get pure executable Python code.
            code = response["response"].replace("python", "").replace("```", "")

            # 4. Execute the Code
            try:
                exec(code)
            except Exception as e:
                # If execution fails, print the error. This goes into our 'buffer'.
                print(f"Error executing generated code: {e}")

            # 5. Restore Output and Check Results
            sys.stdout = old_stdout
            output = buffer.getvalue()

            # 6. Decision Logic
            if "Error executing generated code" in output:
                # FAILURE CASE:
                # The code crashed. We update the 'prompt' variable to include the error message.
                # In the next iteration of the 'while' loop, the LLM will see its previous code AND the error.
                prompt = f"""
The following code has this error: {output} 
Code: 
{code}
"""
                # Inform the user on the UI that we are fixing a bug
                st.markdown(f'Code has Error, fixing... \n{response["response"]} \n {output}' )
            else:
                # SUCCESS CASE:
                # The code ran without throwing an exception.
                st.markdown(f'Code is working well. \n{response["response"]} \n {output}')
                
                # Save the working code to session state so we can ask questions about it later.
                st.session_state["response"] = response["response"]
                # Break the 'while' loop to stop generating.
                break

# --- Part 2: Q&A about the Code ---
# This section allows the user to paste a snippet of the generated code
# and ask "Why did you use this?"
question = st.text_area(label = "Write your question.")
ask = st.button("ASK")

if ask:
    # Display the full working code again for reference
    st.markdown(st.session_state["response"])

    # Construct a new prompt for the LLM specifically for explanation.
    # It includes the user's question, the specific line they asked about,
    # and the full context of the code.
    prompt=f"""
Can you explain why we used this code 
"{question}"
in the following code in very detail step by step:
{st.session_state["response"]}
"""
    # Generate the explanation
    answer = ollama.generate(model='tinyllama:latest',
                               prompt = prompt)

    # Display the explanation
    st.markdown(answer["response"])

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/004.py        
