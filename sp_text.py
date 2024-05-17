import speech_recognition as sr

#filename = "D:\\Speech to Text\\harvard.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.Microphone() as source:
    print("Say Something")
    
    #listen to what user says
    audio_data = r.listen(source)
    
    # recognize (convert from speech to text)
    try:
        text = r.recognize_google(audio_data)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results from Google Speech Recognition service:", e)
    
#Save the user spoken data in a variable
prompt_input = text

# Import necessary modules for language processing
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Initialize the OpenAI language model (LLM)
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

# Create a prompt template for generating prompts
prompt = PromptTemplate(
    input_variables=["input_data"],
    template="Tell me about {input_data} related to Indian states and culture",
)

# Initialize the language model chain (LLMChain)
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain using the input from speech recognition
print(chain.run(prompt_input))
