test = {
  'name': 'Problem 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'd867280d511300bf4fa42dae8866a575',
          'choices': [
            r"""
            All Ant types have a blocks_path attribute that is inherited from
            the Ant superclass
            """,
            'Only the NinjaAnt has a blocks_path attribute',
            'None of the Ant subclasses have a blocks_path attribute',
            'All Ant types except for NinjaAnt have a blocks_path attribute'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which Ant types have a blocks_path attribute?'
        },
        {
          'answer': '0a74e2e9020b74e8968cc9a0ed1ef38d',
          'choices': [
            'blocks_path is True for every Ant subclass except NinjaAnt',
            'blocks_path is False for every Ant subclass except NinjaAnt',
            'blocks_path is True for all Ants',
            'blocks_path is False for all Ants'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the value of blocks_path for each Ant subclass?'
        },
        {
          'answer': 'ad3ed5994969f15b71d99c706bb59339',
          'choices': [
            "When there is an Ant in the Bee's place",
            r"""
            When there is an Ant whose blocks_path attribute is True in the
            Bee's place
            """,
            "When there is not an NinjaAnt in the Bee's place",
            "When there are no Ants in the Bee's place"
          ],
          'hidden': False,
          'locked': True,
          'question': 'When is the path of a Bee blocked?'
        },
        {
          'answer': '484c0146f4f3467577dbd39913dde34b',
          'choices': [
            "Reduces the Bee's armor by the NinjaAnt's damage attribute",
            "Reduces the Bee's armor to 0",
            "Nothing, the NinjaAnt doesn't damage Bees",
            "Blocks the Bee's path"
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does a NinjaAnt do to each Bee that flies in its place?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing NinjaAnt parameters
          >>> ninja = NinjaAnt()
          >>> ninja.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> NinjaAnt.food_cost
          62674984f877ec783f37e8b8b9c264d0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing blocks_path
          >>> NinjaAnt.blocks_path
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> HungryAnt.blocks_path
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> FireAnt.blocks_path
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing NinjaAnts do not block bees
          >>> p0 = gamestate.places["tunnel_0_0"]
          >>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
          >>> bee = Bee(2)
          >>> ninja = NinjaAnt()
          >>> thrower = ThrowerAnt()
          >>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
          >>> p1.add_insect(bee)
          >>> p1.add_insect(ninja)              # Add the Bee and NinjaAnt to p1
          >>> bee.action(gamestate)
          >>> bee.place is ninja.place          # Did NinjaAnt block the Bee from moving?
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> bee.place is p0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> ninja.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> bee.action(gamestate)
          >>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing non-blocking ants do not block bees
          >>> p0 = gamestate.places["tunnel_0_0"]
          >>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
          >>> bee = Bee(2)
          >>> ninja_fire = FireAnt(1)
          >>> ninja_fire.blocks_path = False
          >>> thrower = ThrowerAnt()
          >>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
          >>> p1.add_insect(bee)
          >>> p1.add_insect(ninja_fire)              # Add the Bee and NinjaAnt to p1
          >>> bee.action(gamestate)
          >>> bee.place is ninja_fire.place          # Did the "ninjaish" FireAnt block the Bee from moving?
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> bee.place is p0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> ninja_fire.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> bee.action(gamestate)
          >>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees in its place
          >>> test_place = gamestate.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(2))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(gamestate)   # should strike all bees in place
          >>> [bee.armor for bee in test_place.bees]
          [1, 1, 1]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt doesn't hardcode damage
          >>> test_place = gamestate.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(100))
          >>> ninja = NinjaAnt()
          >>> ninja.damage = 50
          >>> test_place.add_insect(ninja)
          >>> ninja.action(gamestate)   # should strike all bees in place
          >>> [bee.armor for bee in test_place.bees]
          [50, 50, 50]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees, even if some expire
          >>> test_place = gamestate.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(1))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(gamestate)   # should strike all bees in place
          >>> len(test_place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing damage is looked up on the instance
          >>> place = gamestate.places["tunnel_0_0"]
          >>> bee = Bee(900)
          >>> place.add_insect(bee)
          >>> buffNinja = NinjaAnt()
          >>> buffNinja.damage = 500  # Sharpen the sword
          >>> place.add_insect(buffNinja)
          >>> buffNinja.action(gamestate)
          >>> bee.armor
          400
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Ninja ant does not crash when left alone
          >>> ninja = NinjaAnt()
          >>> gamestate.places["tunnel_0_0"].add_insect(ninja)
          >>> ninja.action(gamestate)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Bee does not crash when left alone
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_1"].add_insect(bee)
          >>> bee.action(gamestate)
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
          >>> NinjaAnt.implemented
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
