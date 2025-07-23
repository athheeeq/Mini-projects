def institution_bot(question):
    response = {
        'institution' : 'MITE is a very prestigious institution located in mangalore.',
        'food court' : 'MITE has 2 food courts, one is canteen and another one is food court where you get the items and lunch.',
        'hostel' : 'MITE has a complete residential campus offering the best stay for the inmates.',
        'library' : 'MITE has a fully computerized air conditioned library with rich collections of books.'
    }
    question = question.lower()
    for key in response:
        if key in question:
            return response[key]
    return "I m sorry, I don't have the information in that institution."
        
while True:
    user_input = input("\nAsk a question about the institution : ")
    if user_input.lower() == 'exit':
        break
    response = institution_bot(user_input)
    print(response)