import random
from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def home():
  player_list1 = ['josh', 'mike', 'dan', 'sidney'] 
  player_list2 = ['jordan', 'vitor', 'poch', 'sharon'] 
  player_list3 = ['goodnews', 'racheal', 'dapo','saka']
  player_list4 = ['james', 'mount', 'jack', 'krishno']
  
  ##first round matches
  m1 = []
  m2 = []
  m3 = []
  m4 = []
  m5 = []
  m6 = []
  m7 = []
  m8 = []

  ##
  ###semfinal
  sf1 = []
  sf2 = []
  sf3 = []
  sf4 = []

  ###quarterfinal
  qf1 = []
  qf2 = []

  ##final
  final = []
  for x in range (1):
    
    player1 = random.choice(player_list1)
    m1.append(player1)
    player_list1.remove(player1)

    player2 = random.choice(player_list1)
    m1.append(player2)
    player_list1.remove(player2)



    player3 = random.choice(player_list1)
    m2.append(player3)
    player_list1.remove(player3)

    player4 = random.choice(player_list1)
    m2.append(player4)
    player_list1.remove(player4)


    
    player5 = random.choice(player_list2)
    m3.append(player5)
    player_list2.remove(player5)

    player6 = random.choice(player_list2)
    m3.append(player6)
    player_list2.remove(player6)


    player7 = random.choice(player_list2)
    m4.append(player7)
    player_list2.remove(player7)

    player8 = random.choice(player_list2)
    m4.append(player8)
    player_list2.remove(player8)



    player9 = random.choice(player_list3)
    m5.append(player9)
    player_list3.remove(player9)

    player10 = random.choice(player_list3)
    m5.append(player10)
    player_list3.remove(player10)



    player11 = random.choice(player_list3)
    m6.append(player11)
    player_list3.remove(player11)

    player12 = random.choice(player_list3)
    m6.append(player12)
    player_list3.remove(player12)



    player13 = random.choice(player_list4)
    m7.append(player13)
    player_list4.remove(player13)

    player14 = random.choice(player_list4)
    m7.append(player14)
    player_list4.remove(player14)



    player15 = random.choice(player_list4)
    m8.append(player15)
    player_list4.remove(player15)

    player16 = random.choice(player_list4)
    m8.append(player16)
    player_list4.remove(player16)

    m1w = random.choice(m1)
    m2w = random.choice(m2)
    sf1.append(m1w)
    sf1.append(m2w)

    m3w = random.choice(m3)
    m4w = random.choice(m4)
    sf2.append(m3w)
    sf2.append(m4w)

    m5w = random.choice(m5)
    m6w = random.choice(m6)
    sf3.append(m5w)
    sf3.append(m6w)

    m7w = random.choice(m7)
    m8w = random.choice(m8)
    sf4.append(m7w)
    sf4.append(m8w)

    sf1w = random.choice(sf1)
    sf2w = random.choice(sf2)
    qf1.append(sf1w)
    qf1.append(sf2w)

    sf3w = random.choice(sf3)
    sf4w = random.choice(sf4)
    qf2.append(sf3w)
    qf2.append(sf4w)

    qf1w = random.choice(qf1)
    qf2w = random.choice(qf2)
    final.append(qf1w)
    final.append(qf2w)

    winner = random.choice(final)

  return render_template("index.html", player1=player1, player2=player2, player3=player3, player4=player4, player5=player5, player6=player6, player7=player7, player8=player8, player9=player9, player10=player10, player11=player11, player12=player12, player13=player13, player14=player14, player15=player15, player16=player16, m1w=m1w, m2w=m2w, m3w=m3w, m4w=m4w, m5w=m5w, m6w=m6w, m7w=m7w, m8w=m8w, sf1w=sf1w, sf2w=sf2w, sf3w=sf3w, sf4w=sf4w, qf1w=qf1w, qf2w=qf2w, winner=winner)

app.run(host='0.0.0.0', port=8080, debug=True)










