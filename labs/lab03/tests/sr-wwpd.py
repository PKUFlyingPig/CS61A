test = {
  'name': 'Self-Reference',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def crust():
          ...   print("70km")
          ...   def mantle():
          ...       print("2900km")
          ...       def core():
          ...           print("5300km")
          ...           return mantle()
          ...       return core
          ...   return mantle
          >>> drill = crust
          >>> drill = drill()
          70km
          >>> drill = drill()
          2900km
          >>> drill = drill()
          5300km
          2900km
          >>> drill()
          5300km
          2900km
          Function
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
