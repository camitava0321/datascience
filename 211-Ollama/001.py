"""
Ollama Python Integration - Basic Example
==========================================
This file demonstrates basic usage of the Ollama Python library.
"""

import ollama

def main():
    """
    Main function to demonstrate Ollama usage.
    """
    # Example: List available models
    try:
        models_response = ollama.list()
        print("Available models:")
        
        # The response has a 'models' attribute containing a list of Model objects
        if hasattr(models_response, 'models'):
            for model in models_response.models:
                # Access model attributes directly with null checks
                model_name = model.model if model.model else 'Unknown'
                
                # Calculate size in MB
                if model.size:
                    model_size_mb = model.size / (1024 * 1024)
                    size_str = f"{model_size_mb:.2f} MB"
                else:
                    size_str = "N/A"
                
                # Format modified date
                if model.modified_at:
                    modified = model.modified_at.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    modified = "N/A"
                
                # Get parameter size
                param_size = model.details.parameter_size if model.details else 'N/A'
                
                print(f"  - {model_name}")
                print(f"    Size: {size_str}")
                print(f"    Parameters: {param_size}")
                print(f"    Modified: {modified}")
                print()
        else:
            print("  Models list format not recognized")
            
    except Exception as e:
        print(f"Error listing models: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*50)
    print("Example: Generate a response")
    print("="*50)
    
    # Example: Generate a response with tinyllama
    try:
        response = ollama.generate(
            model='tinyllama:latest',
            prompt='What is Python programming language in one sentence?'
        )
        print(f"\nPrompt: What is Python programming language in one sentence?")
        print(f"Response: {response['response']}")
    except Exception as e:
        print(f"Error generating response: {e}")
        print("Make sure Ollama is running (ollama serve)")


if __name__ == "__main__":
    main()

# Made with Bob
