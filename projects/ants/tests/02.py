test = {
  'name': 'Problem 2',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ba9d5316d8a8cf38d31424fc9bc51ea9',
          'choices': [
            r"""
            A single tile that an Ant can be placed on and that connects to
            other Places
            """,
            'The entire space where the game takes place',
            'The tunnel that bees travel through',
            'Where the bees start out in the game'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does a Place represent in the game?'
        },
        {
          'answer': '010db6ca237fafb71ab37bd963f06870',
          'choices': [
            'When p is constructed',
            'When q is constructed',
            'Never, it is always set to None'
          ],
          'hidden': False,
          'locked': True,
          'question': 'p is a Place whose entrance is q and exit is r (q and r are not None). When is p.entrance first set to a non-None value?'
        },
        {
          'answer': '0be706b6821937577f2e07621737dcb7',
          'choices': [
            'When p is constructed',
            'When q is constructed',
            'Never, it is always set to None'
          ],
          'hidden': False,
          'locked': True,
          'question': 'p is a Place whose entrance is q and exit is r (q and r are not None). When is p.exit first set to a non-None value?'
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> place0 = Place('place_0')
          >>> print(place0.exit)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> print(place0.entrance)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> place1 = Place('place_1', place0)
          >>> place1.exit is place0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> place0.entrance is place1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing if entrances are properly initialized
          >>> tunnel_len = 9
          >>> len(gamestate.bee_entrances)
          1
          >>> tile_1 = gamestate.bee_entrances[0]
          >>> tile_2 = tile_1.exit
          >>> tile_3 = tile_2.exit
          >>> tile_1.entrance is gamestate.beehive
          True
          >>> tile_1.exit is tile_2
          True
          >>> tile_2.entrance is tile_1
          True
          >>> tile_2.exit is tile_3
          True
          >>> tile_3.entrance is tile_2
          True
          >>> tile_3.exit is gamestate.base
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      >>> #
      >>> # Create a test layout where the gamestate is a single row with 3 tiles
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 3)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
