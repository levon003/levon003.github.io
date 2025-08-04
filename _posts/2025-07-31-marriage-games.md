---
layout: post
title:  "Marriage games"
tags: marriage quiz short
excerpt: "A crossword and trivia game for my marriage."
quiz:
  quiz:
  sections:
    - name: "Round 3: Reaching new heights (Zach's round)"
      questions:
        - type: "numeric-range"
          text: "How tall is Mt. Rainier? (in feet)"
          min: 14260
          max: 14560
          explanation: "Mt. Rainier is 14,410 feet tall. We'll give it to you within 150 feet!"
        
        - type: "multiple-choice"
          text: "How many articles are there in the English-language Wikipedia (as of July 2025)?"
          answers:
            - text: "2,000,000"
              correct: false
            - text: "7,000,000"
              correct: true
              explanation: "Wikipedia hit 7 million articles in May 2025!"
            - text: "13,000,000"
              correct: false
            - text: "20,000,000"
              correct: false
        
        - type: "exact-match"
          text: "Zach has two favorite video games. They both were released in 2017 and are playable on the Nintendo Switch console. Name one."
          valid_answers: ["Hollow Knight", "The Legend of Zelda: Breath of the Wild", "The Legend of Zelda", "Breath of the Wild", "BOTW", "LOZ", "Zelda", "Legend of Zelda"]
          explanation: "Zach's two favorite games from 2017 are <i>Hollow Knight</i> and <i>The Legend of Zelda: Breath of the Wild</i>."
        
        - type: "multiple-choice"
          text: "Rock climbing is full of jargon. What does \"crux\" mean?"
          answers:
            - text: "A hitch knot common in climbing"
              correct: false
            - text: "The highest point where the rope is attached to the wall"
              correct: false
            - text: "Accidentally getting assistance from a hold that's not part of the climb"
              correct: false
            - text: "The hardest part of the climb"
              correct: true
              explanation: "The crux is the most difficult section or move on a climbing route."
        
        - type: "numeric-range"
          text: "In what year did reigning chess champion Garry Kasparov first lose to the chess computer Deep Blue?"
          min: 1992
          max: 2002
          explanation: "Kasparov first lost to Deep Blue in 1997. We'll give it to you within five years."

    - name: "Round 4: Food science (Sunita's round)"
      questions:
        - type: "exact-match"
          text: "One of Sunita's research areas is cluster algebras. The main process underlying the combinatorial structure of a cluster algebra is named for the process of alteration in a DNA sequence. What is this process called?"
          valid_answers: ["Mutation"]
          explanation: "No cluster algebras knowledge required!"
        
        - type: "multiple-choice"
          text: "Sunita's favorite berry is the boysenberry: a cross between a raspberry, a blackberry, a dewberry, and a loganberry. Where were boysenberries first created?"
          answers:
            - text: "Washington"
              correct: false
            - text: "Oregon"
              correct: false
            - text: "California"
              correct: true
              explanation: "Boysenberries were first created in California. Oregon is the US state that grows the most boysenberries, New Zealand is the country that grows the most boysenberries, and Washington is where Zach and Sunita got married."
            - text: "New Zealand"
              correct: false
        
        - type: "exact-match"
          text: "Sunita has been to all but five states. Two of the states border Colorado and Texas, two of the states border Ohio and Virginia, and two of the states touch each other at exactly one point. What are the five states?"
          valid_answers: ["New Mexico, Oklahoma, Kentucky, West Virginia, Utah"]
          explanation: "The five states are New Mexico, Oklahoma, Kentucky, West Virginia, and Utah. The quiz validation doesn't support this entry, so give yourself a point if you got it right."
        
        
        - type: "multiple-choice"
          text: "Popcorn increased in popularity during the Great Depression and WWII. Which of the following was NOT a reason why?"
          answers:
            - text: "The introduction of popcorn at movie theaters and the rise of \"talking pictures\""
              correct: false
            - text: "Since popcorn was only 5 to 10 cents a bag, it was a treat most families could still afford"
              correct: false
            - text: "People started eating popcorn for breakfast with milk or cream (as we would eat cereal)"
              correct: true
              explanation: "Trick question: it was already being eaten with milk before the Great Depression!"
            - text: "During WWII, sugar was sent overseas to troops, meaning there was not much candy available in the US"
              correct: false
        
        - type: "exact-match"
          text: "One of Sunita's favorite book club books this past year was Remarkably Bright Creatures, which features an octopus as a main character. While human blood is red because of the iron we use to transport oxygen in our blood, octopus blood is blue because they use what other element to transport oxygen in their blood?"
          valid_answers: ["Copper", "copper"]
          explanation: "Think blue-green like the Statue of Liberty."

    - name: "Round 5: Screen time (Shared media round)"
      questions:
        - type: "numeric-range"
          text: "How many countries – not including the US – have made international versions of The Bachelor?"
          min: 30
          max: 40
          explanation: "35 countries! That's just excessive."
        
        - type: "exact-match"
          text: "In 2019-2020, Zach, Sunita, and Officiant Greg had a subscription to the Broadway on Hennepin series at the Orpheum. The last show they saw before COVID hit was a Lerner and Loewe musical based on the play <i>Pygmalion</i>. What is this show called?"
          valid_answers: ["My Fair Lady"]
          explanation: "The show was <i>My Fair Lady</i>."
        
        - type: "multiple-choice"
          text: "In order to keep the twist of Darth Vader being Luke's father secret, the line \"No, I am your father\" was left out of the script and only told to the actors in the scene. Instead, what did Vader tell Luke happened to his father in the script?"
          answers:
            - text: "\"Your father abandoned you\""
              correct: false
            - text: "\"Obi-Wan killed your father\""
              correct: true
              explanation: "According to ScreenRant: \"In the fake script, Vader’s line was replaced from 'I am your father,' to 'Obi-Wan killed your father.'"
            - text: "\"The Emperor turned him to the Dark Side\""
              correct: false
            - text: "\"Destroying him was all too easy\""
              correct: false
        
        - type: "exact-match"
          text: "Marvel Studios releases its films in groups called \"phases\". Phase 1 began in 2008 with the release of <i>Iron Man</i>. A new Marvel phase started in July 2025. What number is that phase?"
          valid_answers: ["Phase 6", "6"]
          explanation: "Phase 6 started on July 25, 2025 with the release of <i>The Fantastic Four: First Steps</i>."
        
        - type: "exact-match"
          text: "The fictional president in The West Wing is named for the second signatory of the Declaration of Independence. What is his name?"
          valid_answers: ["Josiah Bartlett", "Jed Bartlett"]
          explanation: "Josiah \"Jed\" Bartlett was the second signatory of the Declaration of Independence."

  score_descriptors:
    - min: 86
      text: "You are a: Initiate of the higher mysteries"
    - min: 71
      text: "You are a: Scholar"
    - min: 57
      text: "You are: Distressingly familiar"
    - min: 43
      text: "You are a: Specialist"
    - min: 29
      text: "You are a: Great guesser!"
    - min: 0
      text: "You are: Unlucky"
---

I got married to [Sunita Chepuri](https://sites.google.com/view/sunita-chepuri/home) on July 26, 2025.

Of course, we needed to torment our friends and family with activities.

### Crossword

We created a wedding crossword, which you can complete [on Crosshare](https://crosshare.org/crosswords/ZbnQobmwr3i50mzBEK6K/zachsunita-wedding).

### Trivia

We also designed five rounds of trivia. The first two rounds required specific knowledge of us as a couple, so we're not sharing them publicly here. But the rest are general trivia rounds, so feel free to give them a go below!

{% include quiz.html quiz=page.quiz %}
