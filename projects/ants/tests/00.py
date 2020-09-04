test = {
  'name': 'Problem 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'It represents the amount of health the insect has left, so the insect is eliminated when it reaches 0',
          'choices': [
            r"""
            It represents armor protecting the insect, so the insect can only
            be damaged when its armor reaches 0
            """,
            r"""
            It represents the strength of an insect against attacks, which
            doesn't change throughout the game
            """,
            r"""
            It represents the amount of health the insect has left, so the
            insect is eliminated when it reaches 0
            """
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What is the significance of an Insect's armor attribute? Does this
          value change? If so, how?
          """
        },
        {
          'answer': 'damage',
          'choices': [
            'damage',
            'armor',
            'place',
            'bees'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following is a class attribute of the Insect class?'
        },
        {
          'answer': 'instance, each Ant instance needs its own armor value',
          'choices': [
            'instance, each Ant instance needs its own armor value',
            'instance, each Ant starts out with a different amount of armor',
            'class, Ants of the same subclass all have the same amount of starting armor',
            'class, when one Ant gets damaged, all ants receive the same amount of damage'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Is the armor attribute of the Ant class an instance or class attribute? Why?'
        },
        {
          'answer': 'class, all Ants of the same subclass deal the same damage',
          'choices': [
            'instance, each Ant does damage to bees at different rates',
            'instance, the damage an Ant depends on where the Ant is',
            'class, all Ants of the same subclass deal the same damage',
            'class, all Ants deal the same damage'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
          instance or class attribute? Why?
          """
        },
        {
          'answer': 'Insect',
          'choices': [
            'Insect',
            'Place',
            'Bee',
            'Ant'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which class do both Ant and Bee inherit from?'
        },
        {
          'answer': 'Ants and Bees both have the attributes armor, damage, and place and the methods reduce_armor and action',
          'choices': [
            r"""
            Ants and Bees both have the attributes armor, damage, and place
            and the methods reduce_armor and action
            """,
            r"""
            Ants and Bees both have the attribute damage and the methods
            reduce_armor and action
            """,
            'Ants and Bees both take the same action each turn',
            'Ants and Bees have nothing in common'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What do instances of Ant and instances of Bee have in common?'
        },
        {
          'answer': 'There can be one Ant and many Bees in a single Place',
          'choices': [
            'There can be one Ant and many Bees in a single Place',
            'There can be one Bee and many Ants in a single Place',
            'There is no limit on the number of insects of any type in a single Place',
            'Only one insect can be in a single Place at a time'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many insects can be in a single Place at any given time in the
          game (before Problem 9)?
          """
        },
        {
          'answer': 'The bee stings the ant in its place or moves to the next place if there is no ant in its place',
          'choices': [
            'The bee moves to the next place, then stings the ant in that place',
            'The bee flies to the nearest Ant and attacks it',
            'The bee stings the ant in its place or moves to the next place if there is no ant in its place',
            'The bee stings the ant in its place and then moves to the next place'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does a Bee do during one of its turns?'
        },
        {
          'answer': 'When any bee reaches the end of the tunnel or when the Queen Ant is killed',
          'choices': [
            'When the bees enter the colony',
            'When the colony runs out of food',
            'When any bee reaches the end of the tunnel or when the Queen Ant is killed',
            'When any bee reaches the end of the tunnel and the Queen Ant is killed',
            'When no ants are left on the map'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When is the game lost?'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
