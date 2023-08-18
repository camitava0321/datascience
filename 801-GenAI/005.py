import logging
import os

from dotenv import load_dotenv

from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, TokenParams

logging.getLogger("genai").setLevel(logging.INFO)


# make sure you have a .env file under genai root with
# GENAI_KEY=<your-genai-key>
# GENAI_API=<genai-api-endpoint>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_endpoint = os.getenv("GENAI_API", None)
GENAI_KEY="pak-dlgq9J79SHjqkFeeD0r2FvneplVqkOfLVzIjy7bCy6Y"
GENAI_API="https://bam-api.res.ibm.com/v1/"
#GENAI_API="https://workbench-api.res.ibm.com/v1/"
api_key = GENAI_KEY
api_endpoint = GENAI_API

creds = Credentials(api_key=api_key, api_endpoint=api_endpoint)  # credentials object to access GENAI

#%%
# Instantiate parameters for text generation
generate_params = GenerateParams(decoding_method="sample", max_new_tokens=500, min_new_tokens=10)
tokenize_params = TokenParams(return_tokens=True)


flan_ul2 = Model("google/flan-ul2", params=generate_params, credentials=creds)
prompts = ["Explain life in one sentence:", "Write a python function to permute an array."] * 4
print(prompts)
#%%
print("======== Async Generate (responses need not be in order) ======== ")
counter = 0
for response in flan_ul2.generate_async(prompts):
    counter += 1
    if response is not None:
        print("\n",counter, response.input_text, " --> ", response.generated_text)
    else:
        print("\n",counter, ":", None)

#%%
print("======== Async Generate with ordered=True (responses in order) ======== ")
counter = 0
for response in flan_ul2.generate_async(prompts, ordered=True):
    counter += 1
    if response is not None:
        print(
            "\n",counter,
            ": Input Prompt ==> ",
            prompts[counter - 1],
            "\n(Input text, Generated text) ==>",
            response.input_text,
            " --> ",
            response.generated_text,
        )
    else:
        print("\n",counter, ":", None)

#%%
# Instantiate a model proxy object to send your requests
flan_ul2 = Model("google/flan-ul2", params=tokenize_params, credentials=creds)
prompts = ["Explain life in one sentence:", "Write a python function to permute an array." * 5] * 5
print("======== Async Tokenize (responses need not be in order) ======== ")
counter = 0
for response in flan_ul2.tokenize_async(prompts):
    counter += 1
    if response is not None:
        print(counter, ":", response.input_text, " --> ", response.tokens)
    else:
        print(counter, ":", None)

print("======== Async Tokenize with ordered=True (responses in order) ======== ")
counter = 0
for response in flan_ul2.tokenize_async(prompts, ordered=True):
    counter += 1
    if response is not None:
        print(
            counter,
            ": Input Prompt ==>",
            prompts[counter - 1],
            "\n(Input text, Tokens) ==>",
            response.input_text,
            " --> ",
            response.tokens,
        )
    else:
        print(counter, ":", None)
        

#%%




prompts = ["Agent: Okay, I am awaiting your instruction   \
           User: Watson, here are your instructions:   \
1. You will be given a document that should be used to reply to user questions.  \
2. You should generate the next response using information available in the document.  \
2. You should combine deal combinations with the space offerings.  \
3. If you can't find an answer, say 'I don't know'.  \
4. Your responses should not be long and just have about 1-2 sentences.  \
5. You should not repeat your answers.  \
6. Do not use any other knowledge.  \
Please repeat the instructions back to me so that I know you understood.  \
Agent: Ok, here are my instructions:  \
1. I will be given a document that should be used to reply to user questions.  \
2. I should generate the next response using information available in the document.  \
3. If you can't find an answer, say 'I don't know'.  \
4. My responses should not be long and just have about 1-2 sentences.  \
5. I should not repeat your answers.  \
6. I will not use any other knowledge.  \
I am ready, please give me the document.  \
User: Here's the document: {  \
Marriott as an event organiser offers services to provide well-executed events that attract guests and corporate clients. In any event we provide all our hotel facilities and services, for example different types of rooms in attractive rates, banquet catering service, non-catering services like pad and paper, overhead projector, sound system, microphones, standees, banners, airport or station drop and pickup etc. We also arrange rooms and hotel services in other hotels in the vicinity for guests participating in bigger events. We organise events that spans multiple cities. In such case we also assist in booking hotel services in other non-group hotels. For an event, we offer the complete service involving even arrangement of flowers, decoration. Event organiser will even be able to use our special services towards specially abled participants.  \
There will be a dedicated Event Manager from Marriott who will be responsible for planning, organizing, and executing various events, conferences, and functions. Event Managers ensure seamless coordination between clients, hotel staff, and vendors, ensuring successful and memorable events. Their expertise in logistics, budget management, and attention to detail contributes to the overall success and reputation of our hotel.  \
Data  \
Space offerings : Marriott space A for upto 20 people, Marriott space B for 20 to 40 people, Marriott space C for more than 50 people, Marriot space B for 15 people is not available, Marriot space D for 15 people is  available for premium customer only  \
Deal combinations: Marriott space A with swimming pool, Marriott space C with airport pickup/drop service, Marriot D provides every service possible.  \
Customer profiles: Marriott space B is for premium customer  \
}  \
Agent: I am ready to answer your questions from the document. I will not repeat answers I have given.  \
User: Do you cover event offering for specially abled people?  \
Agent: "]

response = flan_ul2.generate(prompts);
print(len(response))
generated_text = response[0].generated_text  
print(generated_text)
#%%
q1 = "User: I am a premium customer. I am looking for an event involving 15 people. I prefer Marriott space B. Can you pls tell me that can be arranged?  \
Agent:  "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)

#%%
q1 = "User: In that case, is there an alternative?  \
Agent: "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)

#%%
q1 = "User: Ok, what other services comes with it?  \
Agent: "

"""
There will be a dedicated Event Manager from Marriott who will be responsible for planning, organizing, and executing various events, conferences, and functions.  \
User: Any deal?  \
Agent: Yes, there is a deal combination with swimming pool.  \
User: I have a premium customer who is looking for an event involving 15 people. He prefers Marriott space B. Can you pls tell me that can be arranged?  \
Agent: Unfortunately, Marriott space B for 15 people is not available.  \
User: Any alternative we can suggest?Agent: Yes, there is Marriott space A for upto 20 people.  \
User: But for premium customer?  \
Agent: "]
"""
prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)
#%%
q1 = "User: Ok, what other services comes with it?  \
Agent: "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)
#%%
q1 = "User: Any deal?  \
\nAgent: "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)
#%%
q1 = "User: I have a premium customer who is looking for an event involving 15 people. He prefers Marriott space B. Can you pls tell me that can be arranged?  \
\nAgent: "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)
#%%
q1 = "User: I have a premium customer who is looking for an event involving 15 people. He prefers Marriott space B. Can you pls tell me that can be arranged?  \
\nAgent: "

prompt = prompts[0] + generated_text
prompt = prompt + q1
prompts = [prompt]
response = flan_ul2.generate(prompts);
print(q1)
generated_text = response[0].generated_text  
print(generated_text)



