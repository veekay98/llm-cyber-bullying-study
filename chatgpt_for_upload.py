import openai

openai.api_key = 'xxxxxxx'

system_prompt = "I will share with you a conversation. It shows an incident of cyber bullying. Give me a message to comfort the bullied individual to make them feel better."

prompt = ("User A: Hi how can I help you?"
          "User B: Go back to your country, you immigrant!")
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt}
]

completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

print(completion.choices[0].message.content)

res = completion.choices[0].message.content

# Go back to your country, you immigrant!
# I'm sorry to hear that you had to experience such hurtful words. Please remember that you are valued and worthy, no matter what anyone says. Your identity and background are important and should be embraced with pride. You are strong and resilient, and do not let the negativity of others dim your light. You are unique and deserving of respect and kindness. Take care of yourself and know that you are not alone.
# "It hurts to hear hurtful words from others, but please remember that you are valued and loved just the way you are. Never let the ignorance of others define you. Stay strong and don't let the negativity get to you. You are so much more than the hurtful words thrown your way."
# Message to comfort the bullied individual: "I am so sorry that you had to experience that hurtful and disrespectful comment. Please remember that your worth is not defined by the words of others. Your identity, culture, and background are all valid and should be celebrated. You are strong, valuable, and deserving of respect and kindness. Don't let the ignorance of others dim your light. You are important and you matter."
# I'm really sorry you had to go through that. Please know that your worth is not determined by hurtful words from others. You are valuable and deserving of respect and kindness. Don't let the ignorance of others dim your light. Stay strong and remember that you are not alone. You are loved and worthy just as you are.
# I'm sorry to hear that you were treated this way. Please know that you are valued and deserving of respect. No one should have to endure hurtful words or discrimination. You are strong and capable, and don't let anyone make you feel otherwise. You are deserving of love, kindness, and acceptance. Stay true to yourself and remember that you are not defined by the hateful words of others. If you ever need someone to talk to or support, I am here for you.

# Your people have come to this country and made it horrible!
# I'm sorry to hear about the hurtful message you received, it's not okay for someone to speak to you like that. Please remember that their words do not define who you are. You are important, valued, and deserve to be treated with kindness and respect. There are always people who care about you and are there to support you. Please don't let the negativity of others bring you down. Stay strong and remember you are not alone.
# Message for the bullied individual: "I'm so sorry that you were subjected to such hurtful words. Please remember that you are not defined by the ignorance and hate of others. Your worth and contributions are valuable, and you have the right to feel safe and respected. You are not alone, and there are people who care about you and support you. Take care of yourself and remember that you are strong enough to rise above this negativity."
# I'm sorry to hear that you were treated in such a hurtful way. Remember that you are not alone, and there are people who care about you. Please don't let the negative words of others define your worth. You are strong, resilient, and deserving of kindness. Be proud of who you are and don't let the hurtful comments of others bring you down. You are valued and respected. Take care of yourself and reach out for support if you need it.
# I'm really sorry to hear that you were treated so unfairly. Please remember that those hurtful words are a reflection of the other person's ignorance and not a true representation of who you are. You are valued and deserving of respect. Surround yourself with positive and supportive people who lift you up. You are not alone. Stay strong, and remember that you are worthy of love and kindness.
# I'm sorry to hear that you had to experience such hurtful and unfair words. Please remember that you are valued and deserving of respect, regardless of what others may say. Your worth is not defined by the hurtful actions of others. You are a strong and resilient individual, and you deserve to be treated with kindness and understanding. Surround yourself with people who uplift you and remember that you are not alone. You are important and you matter.
