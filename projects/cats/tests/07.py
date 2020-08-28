test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> meowstake_matches("wird", "wiry", big_limit)
          1
          >>> meowstake_matches("wird", "bird", big_limit)
          1
          >>> meowstake_matches("wird", "wir", big_limit)
          1
          >>> meowstake_matches("wird", "bwird", big_limit)
          1
          >>> meowstake_matches("speling", "spelling", big_limit)
          1
          >>> meowstake_matches("used", "use", big_limit)
          1
          >>> meowstake_matches("hash", "ash", big_limit)
          1
          >>> meowstake_matches("ash", "hash", big_limit)
          1
          >>> meowstake_matches("roses", "arose", big_limit)     # roses -> aroses -> arose
          2
          >>> meowstake_matches("tesng", "testing", big_limit)   # tesng -> testng -> testing
          2
          >>> meowstake_matches("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate",
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, meowstake_matches, 10)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, meowstake_matches, 10)
          'abstraction'
          >>> autocorrect("wird", small_words_list, meowstake_matches, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, meowstake_matches, 10)
          'nest'
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
          ...     trace.Trace(trace=True).runfunc(meowstake_matches, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('place', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('pray', 'okee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('cloit', 'cloit', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('yond', 'snd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('tb', 'tb', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('gobi', 'gobi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('watap', 'woitap', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('baffy', 'btfi', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('else', 'konak', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('zygon', 'jzon', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('lar', 'lar', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('shop', 'wopd', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('pc', 'pc', k) > k for k in range(2)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('sail', 'sail', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('fiber', 'fbk', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('doff', 'def', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('meile', 'mqeile', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('donor', 'doinor', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('meet', 'meeu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('tic', 'tih', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('taft', 'hewer', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('moorn', 'toxa', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('hamal', 'hamal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('pridy', 'dance', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('dekko', 'zbk', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('julio', 'juio', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('boist', 'spume', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('jail', 'jaila', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('cumin', 'goes', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('civil', 'whose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('stead', 'ny', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('mikie', 'mdiye', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('utils', 'utils', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('nuque', 'nuq', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('chine', 'ziinx', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('tour', 'erase', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('ak', 'rose', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('sawah', 'shape', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('elb', 'logia', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('noily', 'oibs', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('fluid', 'grad', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('titer', 'tskhteur', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('shood', 'shood', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('sher', 'xdhe', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('dayal', 'qualm', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('tenai', 'whata', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('bow', 'how', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('tony', 'togqq', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('baby', 'ton', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('seron', 'seron', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('tame', 'tfme', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('kissy', 'kisdsxk', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('str', 'st', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('enema', 'nemr', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('beden', 'beden', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('coral', 'coral', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('hack', 'rhack', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('alan', 'alan', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('aru', 'aru', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('tail', 'taiil', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('corps', 'ckcp', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('kazi', 'kazi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('bone', 'bone', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('dee', 'derv', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('fuder', 'fuder', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('harl', 'hhtar', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('def', 'df', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('moio', 'yomo', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('amnia', 'wna', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('pair', 'pair', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('peai', 'eabi', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('pryse', 'prysvf', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('amelu', 'samp', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('weak', 'wk', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('atelo', 'atelo', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('uc', 'kc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('strew', 'jaup', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('dome', 'dume', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('braze', 'sxaze', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('zaman', 'zadpamn', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('twank', 'renne', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('pinky', 'opiky', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('spoke', 'spoke', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('recto', 'recto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('ula', 'ula', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('dame', 'froth', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('grane', 'griae', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('cycad', 'cqcad', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('creem', 'ashreem', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('alky', 'alfy', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('finds', 'fid', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('argot', 'arxgot', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('lc', 'roost', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('mi', 'iran', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('faded', 'fabehc', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('slee', 'ble', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> meowstake_matches('macro', 'macr', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('bbs', 'bbj', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([meowstake_matches('roud', 'roud', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import meowstake_matches, autocorrect
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
