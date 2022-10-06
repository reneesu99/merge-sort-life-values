
ALL_VALUES = ['Acceptance - To be accepted as I am', 'Courtesy - To be considerable and polite towards others', 'Growth - To keep changing and growing', 'Accuracy - To be accurate in my opinions and beliefs', 'Creativity - To have new and original ideas', 'Health - To be physically well and healthy', 'Achievement - To have important accomplishments', 'Dependability - To be reliable and trustworthy', 'Helpfulness - To be helpful to others', 'Adventure - To have new and exciting experiences', 'Duty - To carry out my duties and obligations', 'Honestly - To be honest and truthful', 'Attractiveness - To be physically attractive', 'Ecology - To live in harmony with environment', 'Hope - To maintain a positive and optimistic outlook', 'Authority - To be in charge and responsible for others', 'Excitement - To have a life full of thrills and stimulation', 'Humility - To be modest and unassuming', 'Autonomy - To be self-determined and independent', 'Faithfulness - To be loyal and true in relationship', 'Humor - To see the humorous side of myself and the world', 'Beauty - To appreciate beauty around me', 'Fame - To be known and recognised', 'Independence - To be free from dependence on others', 'Caring - To take care of others', 'Family - To have a happy, loving family', 'Industry - To work hard and well at my life tasks', 'Challenge - To take on difficult task and problems', 'Fitness - To be physically fit and strong', 'Inner Peace - To experience personal peace', 'Change - To have a life full of change and variety', 'Flexibility - To adjust to new circumstances easily', 'Intimacy - To share my innermost experiences with others', 'Comfort - To have a pleasant and comfortable life', 'Forgiveness - To be forgiving of others', 'Justice - To promote fair and equal treatment for all', 'Commitment - To make enduring meaningful commitments', 'Friendship - To have close, supportive friends', 'Knowledge - To learn and contribute valuable knowledge', 'Compassion - To feel and act on concern for others', 'Fun - To play and have fun', 'Leisure - To take to relax and enjoy', 'Contribution - To make a lasting contribution in the world', 'Genuineness - To act in a manner that is true to who I am', 'Loved - To be loved by those close to me', 'Co-operation - To work collaboratively with others', 'God’s Will - To seek and obey the will of God', 'Loving - To give love to others', 'Mastery - To be competent in my everyday activities', 'Responsibility - To make and carry out responsible decisions', 'Tolerance - To accept and respect those who differ from me', 'Mindfulness - To live conscious and mindful of the present moment', 'Risk - To take risks and chances', 'Tradition - To follow respected patterns of the past', 'Moderation - To avoid excesses and find a middle ground', 'Romance - To have intense, exciting love in my life', 'Virtue - To live a morally pure and excellent life', 'Monogamy - To have one close, loving relationship', 'Safety - To be safe and secure', 'Wealth - To have plenty of money', 'Non-Conformity - To question and challenge authority and norms', 'Self-Acceptance - To accept myself as I am', 'World Peace - To work to promote peace in the world', 'Nurturance - To take care of and nurture others', 'Self-Control - To be disciplined in my own actions', 'Openness - To be open to new experiences, ideas, and options', 'Self-Esteem - To feel good about myself', 'Order - To have a life that is well-ordered and organized', 'Self-Knowledge - To have a deep and honest understanding of myself', 'Passion - To have deep feelings about ideas, activities, or people', 'Service - To be of service to others', 'Pleasure - To feel good', 'Sexuality - To have an active and satisfying sex life', 'Popularity - To be well-liked by many people', 'Simplicity - To live simply, with minimal needs', 'Power - To have control over others', 'Solitude - To have time and space where I can be apart from others', 'Purpose - To have meaning and direction in my life', 'Spirituality - To grow and mature spiritually', 'Rationality - To be guided by reason and logic', 'Stability - To have a life that stays daily consistent', 'Realism - To see and act realistically and practically']
MY_VALUES = ["Acceptance - To be accepted as I am",
    "Adventure - To have new and exciting experiences",
    "Autonomy - To be self-determined and independent",
    "Faithfulness - To be loyal and true in relationship",
    "Family - To have a happy, loving family",
    "Health - To be physically well and healthy", 
    "Hope - To maintain a positive and optimistic outlook",
    "Mindfulness - To live conscious and mindful of the present moment ",
    "Moderation - To avoid excesses and find a middle ground",
    "Monogamy - To have one close, loving relationship",
    "Non-Conformity - To question and challenge authority and norms",
    "Pleasure - To feel good",
    "Friendship - To have close, supportive friends",
    "Fun - To play and have fun",
    "Romance - To have intense, exciting love in my life",
    "Self-Knowledge - To have a deep and honest understanding of myself",
    "Simplicity - To live simply, with minimal needs",
    "Independence - To be free from dependence on others", 
    "Inner Peace - To experience personal peace",
    "Intimacy - To share my innermost experiences with others", 
    "Leisure - To take to relax and enjoy",
    "Loved - To be loved by those close to me",
    "Knowledge - To learn and contribute valuable knowledge",
    "Tolerance - To accept and respect those who differ from me"]

def rank_my_values(input_list=None):
    if input_list == None:
        print("Please pass in a list of strings on the function call at line 71. Each string represents a value that you find very important. See MY_VALUES or ALL_VALUES above as examples in formatting. eg rank_my_values(['value1', 'value2', 'value3'])")
        return False
    def merge_sort(input_list):
        mid = len(input_list)//2
        right = input_list[:mid]
        left = input_list[mid:]
        if len(input_list) >1:
            merge_sort(left)
            merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            answer = input(f"1. {left[i]}, or 2. {right[j]}: ")
            if answer == "1":
                input_list[k] = left[i]
                i+=1
                k+=1
            elif answer == "2":
                input_list[k] = right[j]
                j+=1
                k+=1

        while i< len(left):
            input_list[k] = left[i]
            k+=1
            i+=1
        while j< len(right):
            input_list[k] = right[j]
            k+=1
            j+=1
    print("You'll be presented with a series of pairs of values. Please type in '1' or '2' to select which is more important to you. ")
    merge_sort(input_list)
    print(input_list)
    string_value = ""
    for i in range(len(input_list)):
        string_value += f"\n{i+1}. {input_list[i]}"
    print(string_value)

# rank_my_values(["value1", "value2", "value3"])
rank_my_values()
