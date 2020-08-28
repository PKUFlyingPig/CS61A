test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> shifty_shifts("car", "cad", big_limit)
          52f1b72ba99dddc798bb5cebce0be695
          # locked
          >>> shifty_shifts("this", "that", big_limit)
          45c27a29bbaeb163dec9a0eaed9c7c9c
          # locked
          >>> shifty_shifts("one", "two", big_limit)
          91711de69bc1d16e478231c51fac5db8
          # locked
          >>> shifty_shifts("from", "form", big_limit)
          45c27a29bbaeb163dec9a0eaed9c7c9c
          # locked
          >>> shifty_shifts("awe", "awesome", big_limit)
          bfdc03a3c261c5dc71255ec79dd5977e
          # locked
          >>> shifty_shifts("someawe", "awesome", big_limit)
          ca82d3ac444a7724c7a6f8a337e495f5
          # locked
          >>> shifty_shifts("awful", "awesome", big_limit)
          f29bb7189bc0116caaaf05635899b49b
          # locked
          >>> shifty_shifts("awful", "awesome", 3) > 3
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> shifty_shifts("awful", "awesome", 4) > 4
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> shifty_shifts("awful", "awesome", 5) > 5
          81e16d9126cb46b28abbb0a979cb030a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> shifty_shifts("goodbye", "good", big_limit)
          3
          >>> shifty_shifts("pront", "print", big_limit)
          1
          >>> shifty_shifts("misspollid", "misspelled", big_limit)
          2
          >>> shifty_shifts("worry", "word", big_limit)
          2
          >>> shifty_shifts("first", "flashy", big_limit)
          4
          >>> shifty_shifts("hash", "ash", big_limit)
          4
          >>> shifty_shifts("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, shifty_shifts, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, shifty_shifts, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, shifty_shifts, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, shifty_shifts, 10)
          'nest'
          >>> # ban iteration
          >>> test.check('cats.py', 'shifty_shifts', ['While', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(shifty_shifts, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('place', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('pray', 'okee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('cloit', 'cloit', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('yond', 'yo', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('tb', 'tb', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('gobi', 'gobi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('watap', 'wotapi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('baffy', 'bafq', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('else', 'konak', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('zygon', 'zrgoi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('lar', 'lar', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('shop', 'shd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('pc', 'pc', k) > k for k in range(2)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('sail', 'sail', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('fiber', 'fibe', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('doff', 'do', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('meile', 'meilew', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('donor', 'donorc', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('meet', 'meeu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('tic', 'tih', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('taft', 'hewer', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('moorn', 'toxa', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('hamal', 'hamal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('pridy', 'dance', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('dekko', 'ee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('julio', 'juli', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('boist', 'spume', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('jail', 'jailu', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('cumin', 'goes', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('civil', 'whose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('stead', 'ny', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('mikie', 'mdkie', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('utils', 'utils', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('nuque', 'nuquv', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('chine', 'ihi', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('tour', 'erase', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('ak', 'rose', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('sawah', 'shape', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('elb', 'logia', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('noily', 'soi', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('fluid', 'grad', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('titer', 'titegw', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('shood', 'shood', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('sher', 'dhey', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('dayal', 'qualm', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('tenai', 'whata', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('bow', 'how', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('tony', 'togqq', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('baby', 'ton', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('seron', 'seron', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('tame', 'tfme', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('kissy', 'kissykd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('str', 'st', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('enema', 'hnem', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('beden', 'beden', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('coral', 'coral', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('hack', 'haykp', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('alan', 'alan', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('aru', 'aru', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('tail', 'tailp', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('corps', 'co', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('kazi', 'kazi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('bone', 'bone', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('dee', 'dee', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('fuder', 'fuder', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('harl', 'harvn', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('def', 'de', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('moio', 'yomo', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('amnia', 'agni', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('pair', 'pair', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('peai', 'seg', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('pryse', 'pryseffp', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('amelu', 'samp', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('weak', 'wea', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('atelo', 'atelo', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('uc', 'kc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('strew', 'jaup', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('dome', 'dume', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('braze', 'sxaze', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('zaman', 'zaman', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('twank', 'renne', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('pinky', 'pin', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('spoke', 'spoke', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('recto', 'recto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('ula', 'ula', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('dame', 'froth', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('grane', 'gaane', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('cycad', 'cqcad', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('creem', 'creemibh', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('alky', 'alfy', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('finds', 'fond', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('argot', 'argotlp', k) > k for k in range(7)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('lc', 'roost', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('mi', 'iran', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('faded', 'fadedfeb', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('slee', 'ble', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shifty_shifts('macro', 'macr', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('bbs', 'bbj', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([shifty_shifts('roud', 'roud', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import shifty_shifts, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
