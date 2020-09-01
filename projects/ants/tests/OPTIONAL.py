test = {
  'name': 'Problem OPTIONAL',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> ant = HarvesterAnt(2)
          >>> bee1 = Bee(2)
          >>> bee2 = Bee(2)
          >>> bee3 = Bee(2)
          >>> bee4 = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_0"].add_insect(bee4)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_4"].add_insect(ant)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee3)
          >>> laser.action(gamestate)
          >>> round(bee4.armor, 2)
          0.0
          >>> round(bee1.armor, 2)
          0.65
          >>> round(bee2.armor, 2)
          0.7
          >>> round(ant.armor, 2)
          0.95
          >>> round(bee3.armor, 2)
          1.2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> LaserAnt.implemented
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
