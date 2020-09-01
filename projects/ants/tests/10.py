test = {
  'name': 'Problem 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'df9239b5516819d074706715cb1822fe',
          'choices': [
            'A TankAnt does damage to all Bees in its place each turn',
            'A TankAnt has greater armor than a BodyguardAnt',
            'A TankAnt can contain multiple ants',
            'A TankAnt increases the damage of the ant it contains'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Besides costing more to deploy, what is the only difference between a
          TankAnt and a BodyguardAnt?
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
          >>> # Testing TankAnt parameters
          >>> TankAnt.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> TankAnt.damage
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> tank = TankAnt()
          >>> tank.armor
          20d533d3e06345c8bd7072212867f2d1
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
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = gamestate.places['tunnel_0_1']
          >>> other_place = gamestate.places['tunnel_0_2']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(3))
          >>> other_place.add_insect(Bee(3))
          >>> tank.action(gamestate)
          >>> [bee.armor for bee in place.bees]
          [2, 2, 2]
          >>> [bee.armor for bee in other_place.bees]
          [3]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt container methods
          >>> tank = TankAnt()
          >>> thrower = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_1']
          >>> place.add_insect(thrower)
          >>> place.add_insect(tank)
          >>> place.ant is tank
          True
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> tank.action(gamestate)   # Both ants attack bee
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = gamestate.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(1))
          >>> tank.action(gamestate)
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt.damage
          >>> tank = TankAnt()
          >>> tank.damage = 100
          >>> place = gamestate.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(100))
          >>> tank.action(gamestate)
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> tank = TankAnt()
          >>> harvester = HarvesterAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> # Add tank before harvester
          >>> place.add_insect(tank)
          >>> place.add_insect(harvester)
          >>> gamestate.food = 0
          >>> tank.action(gamestate)
          >>> gamestate.food
          1
          >>> try:
          ...   place.add_insect(TankAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          >>> try:
          ...   place.add_insect(HarvesterAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> tank = TankAnt()
          >>> harvester = HarvesterAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> # Add harvester before tank
          >>> place.add_insect(harvester)
          >>> place.add_insect(tank)
          >>> gamestate.food = 0
          >>> tank.action(gamestate)
          >>> gamestate.food
          1
          >>> try:
          ...   place.add_insect(TankAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          >>> try:
          ...   place.add_insect(HarvesterAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Removing ants
          >>> tank = TankAnt()
          >>> test_ant = Ant()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> place.add_insect(test_ant)
          >>> place.remove_insect(test_ant)
          >>> tank.contained_ant is None
          True
          >>> test_ant.place is None
          True
          >>> place.remove_insect(tank)
          >>> place.ant is None
          True
          >>> tank.place is None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tank = TankAnt()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> tank.action(gamestate) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_death_callback = Insect.death_callback
          >>> Insect.death_callback = lambda x: print("insect died")
          >>> place = gamestate.places["tunnel_0_0"]
          >>> bee = Bee(3)
          >>> tank = TankAnt()
          >>> ant = ThrowerAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> place.add_insect(tank)
          >>> bee.action(gamestate)
          >>> bee.action(gamestate)
          insect died
          >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_armor or Insect.reduce_armor
          insect died
          >>> Insect.death_callback = original_death_callback
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> TankAnt.implemented
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
