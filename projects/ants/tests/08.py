test = {
  'name': 'Problem 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '64cb170acd2b167609e6df7dd048fd96',
          'choices': [
            'Ant',
            'ThrowerAnt',
            'NinjaAnt',
            'The WallAnt class does not inherit from any class'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What class does WallAnt inherit from?'
        },
        {
          'answer': '342b4efa1ef6de0defc39dc4fbf1ebf1',
          'choices': [
            'A WallAnt takes no action each turn',
            'A WallAnt increases its own armor by 1 each turn',
            'A WallAnt reduces its own armor by 1 each turn',
            'A WallAnt attacks all the Bees in its place each turn'
          ],
          'hidden': False,
          'locked': True,
          'question': "What is a WallAnt's action?"
        },
        {
          'answer': '50be1539e31a90ea01dbc6bf87f83b9f',
          'choices': [
            'Ant subclasses inherit the action method from the Insect class',
            'Ant subclasses inherit the action method from the Ant class',
            'Ant subclasses do not inherit the action method from any class'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Where do Ant subclasses inherit the action method from?'
        },
        {
          'answer': 'c3962b43bab9946b4984107f5e53e9e7',
          'choices': [
            'Nothing',
            'Throw a leaf at the nearest Bee',
            'Move to the next place',
            'Reduce the armor of all Bees in its place'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If a subclass of Ant does not override the action method, what is the
          default action?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing WallAnt parameters
          >>> wall = WallAnt()
          >>> wall.name
          b344415ec12ae63ab2f69b87a119dba6
          # locked
          >>> wall.armor
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> # `armor` should not be a class attribute
          >>> not hasattr(WallAnt, 'armor')
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> WallAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = Ant.__init__
          >>> Ant.__init__ = lambda self, armor: print("init") #If this errors, you are not calling the parent constructor correctly.
          >>> wall = WallAnt()
          init
          >>> Ant.__init__ = original
          >>> wall = WallAnt()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing WallAnt holds strong
          >>> beehive, layout = Hive(AssaultPlan()), dry_layout
          >>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
          >>> place = gamestate.places['tunnel_0_4']
          >>> wall = WallAnt()
          >>> bee = Bee(1000)
          >>> place.add_insect(wall)
          >>> place.add_insect(bee)
          >>> for i in range(3):
          ...     bee.action(gamestate)
          ...     wall.action(gamestate)   # WallAnt does nothing
          >>> wall.armor
          1
          >>> bee.armor
          1000
          >>> wall.place is place
          True
          >>> bee.place is place
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> WallAnt.implemented
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
