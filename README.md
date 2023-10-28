# Simple-Text-Inpainting-System
In this work, we bring about the idea of text inpainting, and design a system for text inpainting task using simple easy sentences and zero shot learning. We demonstrate our method to get dataset and implement the system with limited time and resource, making use of LLM. We also conduct a set of evaluations.

Here we define text inpainting as the same task: For some text materials, given a key word is changed to new word with different meaning, slightly modify the parts of the text other than the key word, to make the resulting sentence reasonable, while changing the original text to the least extent. 

For example, the initial text: "I **hate** eating ducks. **They are my greatest fears.**" The key word is chosen as "hate", and replaced with a new word "love". 

The resulting inpainted text would be: "I **love** eating ducks. **They are my favorite food.**" 

Note that the text "I love eating ducks. Ducks are delicious." seems like a reasonable result, but the idea of text inpainting is to reduce the change of the original text as little as possible, so the latter sentence is not a good answer.

This is a course project of NLP (SI630) in UofM.
For a detailed report about this project, see: [textinpaint.pdf](https://github.com/KolvacS-W/Simple-Text-Inpainting-System/files/13196700/textinpaint.pdf) and the provided code.

<img width="1035" alt="Screen Shot 2023-10-28 at 4 46 25 PM" src="https://github.com/KolvacS-W/Simple-Text-Inpainting-System/assets/55591358/484ca325-4cdc-408b-938a-3472f31afae8">
