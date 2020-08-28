test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['short', 'really long', 'tiny']
          >>> s = lambda p: len(p) <= 5
          >>> choose(ps, s, 0)
          93686a32597db396f8ea27f37f3e77dd
          # locked
          >>> choose(ps, s, 1)
          91ddcb514fd8cd4a80c84840972e0693
          # locked
          >>> choose(ps, s, 2)
          ff4fea29a1875949726ebf30fc8c6cba
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['d', 'Njtv', 'Kxg', 'ym6bMNxUy', 'Lz']
          >>> s = lambda p: p == 'Kxg' or p == 'Lz' or p == 'd'
          >>> choose(ps, s, 0)
          'd'
          >>> choose(ps, s, 1)
          'Kxg'
          >>> choose(ps, s, 2)
          'Lz'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['jlfpaqbmh', 'zYuLsul', 'exx', 'X3EGwnPjh9', '5ba8riy']
          >>> s = lambda p: p == '5ba8riy' or p == 'exx' or p == 'jlfpaqbmh' or p == 'zYuLsul'
          >>> choose(ps, s, 0)
          'jlfpaqbmh'
          >>> choose(ps, s, 1)
          'zYuLsul'
          >>> choose(ps, s, 2)
          'exx'
          >>> choose(ps, s, 3)
          '5ba8riy'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['wRslOhIXF', 'VFAu80', 'NdMeQR', 'NMQH', 'fyeU', 'Ft5Fcq0', 'eAp', 'NU']
          >>> s = lambda p: p == 'Ft5Fcq0' or p == 'NdMeQR' or p == 'eAp' or p == 'fyeU'
          >>> choose(ps, s, 0)
          'NdMeQR'
          >>> choose(ps, s, 1)
          'fyeU'
          >>> choose(ps, s, 2)
          'Ft5Fcq0'
          >>> choose(ps, s, 3)
          'eAp'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['d4iav9tkR5', 'kv3MGuSDNo', 'ArAwcc8bZ', 'OUHDQy', '4RH7pWLu', 'vo', 'C32aa', 's0L44hL9UH']
          >>> s = lambda p: p == '4RH7pWLu' or p == 'ArAwcc8bZ' or p == 'C32aa' or p == 'OUHDQy' or p == 'd4iav9tkR5' or p == 'kv3MGuSDNo'
          >>> choose(ps, s, 0)
          'd4iav9tkR5'
          >>> choose(ps, s, 1)
          'kv3MGuSDNo'
          >>> choose(ps, s, 2)
          'ArAwcc8bZ'
          >>> choose(ps, s, 3)
          'OUHDQy'
          >>> choose(ps, s, 4)
          '4RH7pWLu'
          >>> choose(ps, s, 5)
          'C32aa'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['bOxiYj', 'TE335OKY', 'Q0da3vv', 'M9M4cU1EiX', '6xG', 'ZQTHGTCdY', 'pIF5']
          >>> s = lambda p: p == '6xG' or p == 'Q0da3vv' or p == 'ZQTHGTCdY' or p == 'bOxiYj' or p == 'pIF5'
          >>> choose(ps, s, 0)
          'bOxiYj'
          >>> choose(ps, s, 1)
          'Q0da3vv'
          >>> choose(ps, s, 2)
          '6xG'
          >>> choose(ps, s, 3)
          'ZQTHGTCdY'
          >>> choose(ps, s, 4)
          'pIF5'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['2qjiKNB', 'E', 'h']
          >>> s = lambda p: p == 'E' or p == 'h'
          >>> choose(ps, s, 0)
          'E'
          >>> choose(ps, s, 1)
          'h'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['uQTp', 'z', 'ln', 'AVHSUeHicm', 'BFcf9', 'wYRfLXeLqc', 'tv8', 'fYAo3OfgQA', 'vlbs']
          >>> s = lambda p: p == 'AVHSUeHicm' or p == 'BFcf9' or p == 'ln' or p == 'uQTp' or p == 'vlbs'
          >>> choose(ps, s, 0)
          'uQTp'
          >>> choose(ps, s, 1)
          'ln'
          >>> choose(ps, s, 2)
          'AVHSUeHicm'
          >>> choose(ps, s, 3)
          'BFcf9'
          >>> choose(ps, s, 4)
          'vlbs'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['2dtxNC5oxi', 'UQAiNMeWhS', 'l', '6gt8Sf4y']
          >>> s = lambda p: p == '2dtxNC5oxi' or p == '6gt8Sf4y' or p == 'UQAiNMeWhS'
          >>> choose(ps, s, 0)
          '2dtxNC5oxi'
          >>> choose(ps, s, 1)
          'UQAiNMeWhS'
          >>> choose(ps, s, 2)
          '6gt8Sf4y'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['XPfAi', 'OWTv', 'Zk']
          >>> s = lambda p: p == 'XPfAi' or p == 'Zk'
          >>> choose(ps, s, 0)
          'XPfAi'
          >>> choose(ps, s, 1)
          'Zk'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['47w9bw0', '6X41BHDCa', 'k4DQ84msw', 'b4JlLtM3j', '4']
          >>> s = lambda p: p == '4' or p == '47w9bw0' or p == '6X41BHDCa' or p == 'b4JlLtM3j'
          >>> choose(ps, s, 0)
          '47w9bw0'
          >>> choose(ps, s, 1)
          '6X41BHDCa'
          >>> choose(ps, s, 2)
          'b4JlLtM3j'
          >>> choose(ps, s, 3)
          '4'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['paX7C', 'DWDX6ijaQO', 'KZqKVl2', 'R6HiKoXZ2', 'nZznCw', 'mbF5KBsDnw', 'E4lCkyjp', 'q2h', 'lrUhlCHu6']
          >>> s = lambda p: p == 'R6HiKoXZ2' or p == 'mbF5KBsDnw'
          >>> choose(ps, s, 0)
          'R6HiKoXZ2'
          >>> choose(ps, s, 1)
          'mbF5KBsDnw'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['B', '3n', 'hs', 'TCW9GTS9e', 'mbk', '1NurBy', 'rdgRYYa9p', 'x', 'zRk5BS1']
          >>> s = lambda p: p == '3n' or p == 'TCW9GTS9e' or p == 'hs' or p == 'x'
          >>> choose(ps, s, 0)
          '3n'
          >>> choose(ps, s, 1)
          'hs'
          >>> choose(ps, s, 2)
          'TCW9GTS9e'
          >>> choose(ps, s, 3)
          'x'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['cd', 'mWwX', 'fnzIl', 'ka1Omns', 'JKJHE3GswY', 'u']
          >>> s = lambda p: p == 'JKJHE3GswY' or p == 'fnzIl' or p == 'ka1Omns' or p == 'mWwX'
          >>> choose(ps, s, 0)
          'mWwX'
          >>> choose(ps, s, 1)
          'fnzIl'
          >>> choose(ps, s, 2)
          'ka1Omns'
          >>> choose(ps, s, 3)
          'JKJHE3GswY'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['k', 'M']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['h5MQCkq', 'TAzx2RG3e', 'w', 'fL4LP', 'NdpenT74r', 'aFj7B1A', 'Yb8hOkT', 'b5ln']
          >>> s = lambda p: p == 'NdpenT74r' or p == 'TAzx2RG3e' or p == 'Yb8hOkT' or p == 'aFj7B1A' or p == 'b5ln' or p == 'h5MQCkq' or p == 'w'
          >>> choose(ps, s, 0)
          'h5MQCkq'
          >>> choose(ps, s, 1)
          'TAzx2RG3e'
          >>> choose(ps, s, 2)
          'w'
          >>> choose(ps, s, 3)
          'NdpenT74r'
          >>> choose(ps, s, 4)
          'aFj7B1A'
          >>> choose(ps, s, 5)
          'Yb8hOkT'
          >>> choose(ps, s, 6)
          'b5ln'
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['mf3aCB', 'lv2VDrTF', 'GkpePNLt', 'p4YXbFG', 'AIlYbO', 'gPIOwO', 'CJehcQGLh', 'yL8T']
          >>> s = lambda p: p == 'AIlYbO' or p == 'CJehcQGLh' or p == 'gPIOwO' or p == 'lv2VDrTF' or p == 'mf3aCB'
          >>> choose(ps, s, 0)
          'mf3aCB'
          >>> choose(ps, s, 1)
          'lv2VDrTF'
          >>> choose(ps, s, 2)
          'AIlYbO'
          >>> choose(ps, s, 3)
          'gPIOwO'
          >>> choose(ps, s, 4)
          'CJehcQGLh'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['fb7e9FePGq', '6Us0GbFkI', 'oDnaL', '7SZ', 'ILPKrO0So', 'F27VNv', 'Sq2ivsu5S', 'byR', 'PbU7Rgrm']
          >>> s = lambda p: p == '6Us0GbFkI' or p == 'F27VNv' or p == 'PbU7Rgrm' or p == 'Sq2ivsu5S' or p == 'fb7e9FePGq'
          >>> choose(ps, s, 0)
          'fb7e9FePGq'
          >>> choose(ps, s, 1)
          '6Us0GbFkI'
          >>> choose(ps, s, 2)
          'F27VNv'
          >>> choose(ps, s, 3)
          'Sq2ivsu5S'
          >>> choose(ps, s, 4)
          'PbU7Rgrm'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['w5WTwFe']
          >>> s = lambda p: p == 'w5WTwFe'
          >>> choose(ps, s, 0)
          'w5WTwFe'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['fXUYciyIr', 'vVQk01', 'KeRbdjfo']
          >>> s = lambda p: p == 'vVQk01'
          >>> choose(ps, s, 0)
          'vVQk01'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Ot0', '4wI', 'HkwYSN', 'qNhjljev', 'NCrXc1']
          >>> s = lambda p: p == '4wI' or p == 'HkwYSN' or p == 'Ot0'
          >>> choose(ps, s, 0)
          'Ot0'
          >>> choose(ps, s, 1)
          '4wI'
          >>> choose(ps, s, 2)
          'HkwYSN'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['ulwhIG2OvA', 'q9MM', 'P']
          >>> s = lambda p: p == 'P' or p == 'q9MM' or p == 'ulwhIG2OvA'
          >>> choose(ps, s, 0)
          'ulwhIG2OvA'
          >>> choose(ps, s, 1)
          'q9MM'
          >>> choose(ps, s, 2)
          'P'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['eWW4J8IXk', 'US99P926W', 'Mu7u3', 'PfMLsgY4S', 'W1f', '6', 'W4BH', 's', 'uACjqTa']
          >>> s = lambda p: p == '6' or p == 'Mu7u3' or p == 'PfMLsgY4S' or p == 'US99P926W' or p == 'eWW4J8IXk'
          >>> choose(ps, s, 0)
          'eWW4J8IXk'
          >>> choose(ps, s, 1)
          'US99P926W'
          >>> choose(ps, s, 2)
          'Mu7u3'
          >>> choose(ps, s, 3)
          'PfMLsgY4S'
          >>> choose(ps, s, 4)
          '6'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['SaKM2', 'iFKDs', '6DNIPiOfV', 'IDsrM', 'ttcBhBNxUQ']
          >>> s = lambda p: p == '6DNIPiOfV' or p == 'SaKM2' or p == 'iFKDs' or p == 'ttcBhBNxUQ'
          >>> choose(ps, s, 0)
          'SaKM2'
          >>> choose(ps, s, 1)
          'iFKDs'
          >>> choose(ps, s, 2)
          '6DNIPiOfV'
          >>> choose(ps, s, 3)
          'ttcBhBNxUQ'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Oj2OFTm', 'AzZg7TmX', 'lvf']
          >>> s = lambda p: p == 'lvf'
          >>> choose(ps, s, 0)
          'lvf'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['axrr', 'K7']
          >>> s = lambda p: p == 'axrr'
          >>> choose(ps, s, 0)
          'axrr'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['xSY9iCe', '9F0fbNdy3d', 'TdbwF', 'V']
          >>> s = lambda p: p == 'V' or p == 'xSY9iCe'
          >>> choose(ps, s, 0)
          'xSY9iCe'
          >>> choose(ps, s, 1)
          'V'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['WbMtnAG', 'ITr3Z', 'z0UyvE', 'MVB4sV1m', '6']
          >>> s = lambda p: p == '6'
          >>> choose(ps, s, 0)
          '6'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['iF4WLyznX', 'QHU', 'e2']
          >>> s = lambda p: p == 'QHU' or p == 'e2' or p == 'iF4WLyznX'
          >>> choose(ps, s, 0)
          'iF4WLyznX'
          >>> choose(ps, s, 1)
          'QHU'
          >>> choose(ps, s, 2)
          'e2'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['fw0GdxmaZx']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['S9IO', 'P', 'yv', 'HEE4', 'lB']
          >>> s = lambda p: p == 'HEE4' or p == 'S9IO'
          >>> choose(ps, s, 0)
          'S9IO'
          >>> choose(ps, s, 1)
          'HEE4'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['TT0mxc', '7rUdPh', 'bXT9Jss0', 'MmqgB', 'l']
          >>> s = lambda p: p == '7rUdPh' or p == 'MmqgB' or p == 'TT0mxc'
          >>> choose(ps, s, 0)
          'TT0mxc'
          >>> choose(ps, s, 1)
          '7rUdPh'
          >>> choose(ps, s, 2)
          'MmqgB'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['qIx6C8DM', 'sszrxRC']
          >>> s = lambda p: p == 'qIx6C8DM'
          >>> choose(ps, s, 0)
          'qIx6C8DM'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['28yt8h', 'dLQjelrdbI', 'yQsk', 'YKK5f', 'Mnll4AD0DA', 'l', 'UEePEqt']
          >>> s = lambda p: p == 'Mnll4AD0DA' or p == 'UEePEqt' or p == 'YKK5f' or p == 'dLQjelrdbI'
          >>> choose(ps, s, 0)
          'dLQjelrdbI'
          >>> choose(ps, s, 1)
          'YKK5f'
          >>> choose(ps, s, 2)
          'Mnll4AD0DA'
          >>> choose(ps, s, 3)
          'UEePEqt'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['ycsj5dM9', 'o8QT', 'HnFS', 'mlwqqQM2']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['2veJflQoDs']
          >>> s = lambda p: p == '2veJflQoDs'
          >>> choose(ps, s, 0)
          '2veJflQoDs'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['HSa5Oll4', '53ESB34aP', 'Vvd', 'tjT7', 'Nf4gq9E8S', '5k', 'EGQIsv4dqA', 'HdD26', 'VstrT']
          >>> s = lambda p: p == '53ESB34aP' or p == '5k' or p == 'HdD26'
          >>> choose(ps, s, 0)
          '53ESB34aP'
          >>> choose(ps, s, 1)
          '5k'
          >>> choose(ps, s, 2)
          'HdD26'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['EOH', 'L3gKaBFggw', 'Pw', '8KotZ', 'ETvnL8wUFz']
          >>> s = lambda p: p == '8KotZ' or p == 'ETvnL8wUFz' or p == 'L3gKaBFggw'
          >>> choose(ps, s, 0)
          'L3gKaBFggw'
          >>> choose(ps, s, 1)
          '8KotZ'
          >>> choose(ps, s, 2)
          'ETvnL8wUFz'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['6JdQvy1', 'FiOdYmyU', 'yA', 'y0Xk', 'cZCJ']
          >>> s = lambda p: p == 'FiOdYmyU' or p == 'cZCJ' or p == 'yA'
          >>> choose(ps, s, 0)
          'FiOdYmyU'
          >>> choose(ps, s, 1)
          'yA'
          >>> choose(ps, s, 2)
          'cZCJ'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['t8ecHx']
          >>> s = lambda p: p == 't8ecHx'
          >>> choose(ps, s, 0)
          't8ecHx'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['PaugJ7We7l', 'EruzGoKuu', 'gfSxiiinxX', 'xT2EnjKnF4', '4dHOOOn', 'mPOFazJth', 'H2qc', 'bcHVrkfbu0', 'QV']
          >>> s = lambda p: p == 'H2qc' or p == 'bcHVrkfbu0' or p == 'mPOFazJth'
          >>> choose(ps, s, 0)
          'mPOFazJth'
          >>> choose(ps, s, 1)
          'H2qc'
          >>> choose(ps, s, 2)
          'bcHVrkfbu0'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['L44YbmhY', 'Fk3t', 'GX1ji0EpoC', 'O6kwd', 'h3Xt', 'sYp6dE']
          >>> s = lambda p: p == 'O6kwd' or p == 'h3Xt' or p == 'sYp6dE'
          >>> choose(ps, s, 0)
          'O6kwd'
          >>> choose(ps, s, 1)
          'h3Xt'
          >>> choose(ps, s, 2)
          'sYp6dE'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['CoQh', 'M5swk', '0JNxcv0b', 'RDLb7uGl', 'v8RyWA6PB7', 'R2Z']
          >>> s = lambda p: p == 'CoQh'
          >>> choose(ps, s, 0)
          'CoQh'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['X', '6qZr7B', 'UEx', 'J']
          >>> s = lambda p: p == 'J' or p == 'UEx' or p == 'X'
          >>> choose(ps, s, 0)
          'X'
          >>> choose(ps, s, 1)
          'UEx'
          >>> choose(ps, s, 2)
          'J'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['XT7d', 'u', 'VQ4x', 'wzdhdJMT']
          >>> s = lambda p: p == 'VQ4x' or p == 'XT7d' or p == 'wzdhdJMT'
          >>> choose(ps, s, 0)
          'XT7d'
          >>> choose(ps, s, 1)
          'VQ4x'
          >>> choose(ps, s, 2)
          'wzdhdJMT'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['F', 'Je54pb', '52ixUi']
          >>> s = lambda p: p == 'F'
          >>> choose(ps, s, 0)
          'F'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['06tslD8Bq', 'iGF', 'wI7pEIcY', 'xi428Wc', 'OimbC']
          >>> s = lambda p: p == '06tslD8Bq' or p == 'OimbC'
          >>> choose(ps, s, 0)
          '06tslD8Bq'
          >>> choose(ps, s, 1)
          'OimbC'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['hiiZqx7', 'h', 'TX3YAYRb', '70iPYPb1', 'j', 'acU', 'eJ']
          >>> s = lambda p: p == '70iPYPb1' or p == 'TX3YAYRb' or p == 'eJ' or p == 'h'
          >>> choose(ps, s, 0)
          'h'
          >>> choose(ps, s, 1)
          'TX3YAYRb'
          >>> choose(ps, s, 2)
          '70iPYPb1'
          >>> choose(ps, s, 3)
          'eJ'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['20Ymff', 'sK', 's', 'Ag7H', 'KpCpiJO', '7eme86FfN4', 'ng', 'TL0Ek']
          >>> s = lambda p: p == '20Ymff' or p == 'Ag7H' or p == 'TL0Ek' or p == 's'
          >>> choose(ps, s, 0)
          '20Ymff'
          >>> choose(ps, s, 1)
          's'
          >>> choose(ps, s, 2)
          'Ag7H'
          >>> choose(ps, s, 3)
          'TL0Ek'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['GjfqvE', 'PL6UL', 'KJBMC', 'kgzHn', 'NWyO2', 'Cf5sl', '8Exh', 'B94I', 'E3rd1T']
          >>> s = lambda p: p == '8Exh' or p == 'B94I' or p == 'Cf5sl' or p == 'NWyO2' or p == 'PL6UL' or p == 'kgzHn'
          >>> choose(ps, s, 0)
          'PL6UL'
          >>> choose(ps, s, 1)
          'kgzHn'
          >>> choose(ps, s, 2)
          'NWyO2'
          >>> choose(ps, s, 3)
          'Cf5sl'
          >>> choose(ps, s, 4)
          '8Exh'
          >>> choose(ps, s, 5)
          'B94I'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['wC3GfQlB', 'JHJH', 'XqlW2U', 'mN5KwhN', 'uI1Rouka']
          >>> s = lambda p: p == 'JHJH' or p == 'XqlW2U' or p == 'uI1Rouka' or p == 'wC3GfQlB'
          >>> choose(ps, s, 0)
          'wC3GfQlB'
          >>> choose(ps, s, 1)
          'JHJH'
          >>> choose(ps, s, 2)
          'XqlW2U'
          >>> choose(ps, s, 3)
          'uI1Rouka'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['L79w0W', '6mj6fs6zl', 'JMAx5', 'TAxJlgomqw', 'VqC', 'v77m', 'L', 'fGNj28', 'n0FiOnb']
          >>> s = lambda p: p == 'JMAx5' or p == 'L79w0W' or p == 'TAxJlgomqw'
          >>> choose(ps, s, 0)
          'L79w0W'
          >>> choose(ps, s, 1)
          'JMAx5'
          >>> choose(ps, s, 2)
          'TAxJlgomqw'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['pxH', '4', 'rjgP3e00', 'uqM4zxd', 'bs2']
          >>> s = lambda p: p == '4' or p == 'rjgP3e00'
          >>> choose(ps, s, 0)
          '4'
          >>> choose(ps, s, 1)
          'rjgP3e00'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['9D9L3LBH2', 'J', 'VhFH13iZk', 'DBa3RTBs', 'yW', 'k877CPSy0', 'n0P69H']
          >>> s = lambda p: p == '9D9L3LBH2' or p == 'k877CPSy0' or p == 'n0P69H' or p == 'yW'
          >>> choose(ps, s, 0)
          '9D9L3LBH2'
          >>> choose(ps, s, 1)
          'yW'
          >>> choose(ps, s, 2)
          'k877CPSy0'
          >>> choose(ps, s, 3)
          'n0P69H'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['paIR6', '7xwK5A3VXy', 'RlU', '1', 'HzkFCL1']
          >>> s = lambda p: p == '1' or p == '7xwK5A3VXy' or p == 'HzkFCL1'
          >>> choose(ps, s, 0)
          '7xwK5A3VXy'
          >>> choose(ps, s, 1)
          '1'
          >>> choose(ps, s, 2)
          'HzkFCL1'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['wp4I4O', '35', 'ilyr69', 'IW', 'ge', 'z2YoOA']
          >>> s = lambda p: p == '35' or p == 'ge'
          >>> choose(ps, s, 0)
          '35'
          >>> choose(ps, s, 1)
          'ge'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['x', 'ovJ0zHALaM', 'uQ8ca']
          >>> s = lambda p: p == 'uQ8ca' or p == 'x'
          >>> choose(ps, s, 0)
          'x'
          >>> choose(ps, s, 1)
          'uQ8ca'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Rp15aFda']
          >>> s = lambda p: p == 'Rp15aFda'
          >>> choose(ps, s, 0)
          'Rp15aFda'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['kpJi5rI']
          >>> s = lambda p: p == 'kpJi5rI'
          >>> choose(ps, s, 0)
          'kpJi5rI'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['IqV', '7Qb', 'fTVSZxW5']
          >>> s = lambda p: p == '7Qb' or p == 'fTVSZxW5'
          >>> choose(ps, s, 0)
          '7Qb'
          >>> choose(ps, s, 1)
          'fTVSZxW5'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['rjZl61rKE', 'HDjOZ1']
          >>> s = lambda p: p == 'rjZl61rKE'
          >>> choose(ps, s, 0)
          'rjZl61rKE'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['sGraoBYg', 'oLA4', 'yvOQGzZ', 'hLPo8k0gen']
          >>> s = lambda p: p == 'hLPo8k0gen' or p == 'yvOQGzZ'
          >>> choose(ps, s, 0)
          'yvOQGzZ'
          >>> choose(ps, s, 1)
          'hLPo8k0gen'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['3M2X0Zv', 'F', 'k2DiIqXEK', 'gu9']
          >>> s = lambda p: p == '3M2X0Zv' or p == 'F' or p == 'k2DiIqXEK'
          >>> choose(ps, s, 0)
          '3M2X0Zv'
          >>> choose(ps, s, 1)
          'F'
          >>> choose(ps, s, 2)
          'k2DiIqXEK'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['vh4DgMbOL', 'p4', 'XASk3gAAVQ', 'tielaIdpE', 'Dw']
          >>> s = lambda p: p == 'Dw' or p == 'vh4DgMbOL'
          >>> choose(ps, s, 0)
          'vh4DgMbOL'
          >>> choose(ps, s, 1)
          'Dw'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Z6npAvZk', 'N', 'VFAkGss', 'gG7']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['kfhzjB', 'wzTJ', 'O1JE2KF3']
          >>> s = lambda p: p == 'O1JE2KF3' or p == 'wzTJ'
          >>> choose(ps, s, 0)
          'wzTJ'
          >>> choose(ps, s, 1)
          'O1JE2KF3'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['KkSWCyxu', 'mStVtBi']
          >>> s = lambda p: p == 'KkSWCyxu' or p == 'mStVtBi'
          >>> choose(ps, s, 0)
          'KkSWCyxu'
          >>> choose(ps, s, 1)
          'mStVtBi'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['RA3uXwj4HM', 'y', 'Q0l1dq', 'ycJNy4V5', 'JRwovXgf', 'WTqDQ7Qt']
          >>> s = lambda p: p == 'JRwovXgf' or p == 'Q0l1dq' or p == 'RA3uXwj4HM'
          >>> choose(ps, s, 0)
          'RA3uXwj4HM'
          >>> choose(ps, s, 1)
          'Q0l1dq'
          >>> choose(ps, s, 2)
          'JRwovXgf'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['y87', '0', 'vU1uNi', 'x', 'HuY2b', 'p']
          >>> s = lambda p: p == '0' or p == 'p' or p == 'vU1uNi'
          >>> choose(ps, s, 0)
          '0'
          >>> choose(ps, s, 1)
          'vU1uNi'
          >>> choose(ps, s, 2)
          'p'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['OsFHq6MHE', 'jaiB', 'O', 'Wm', 'UWsHRw', '7wQ', 'cSX22kpZ']
          >>> s = lambda p: p == '7wQ' or p == 'O' or p == 'UWsHRw'
          >>> choose(ps, s, 0)
          'O'
          >>> choose(ps, s, 1)
          'UWsHRw'
          >>> choose(ps, s, 2)
          '7wQ'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['UkLE', 'pAVhDv', 'qiC1bA8ah', 'S', 'O90', 'd5p', 'F2', 'LE']
          >>> s = lambda p: p == 'LE' or p == 'O90' or p == 'S' or p == 'UkLE' or p == 'd5p'
          >>> choose(ps, s, 0)
          'UkLE'
          >>> choose(ps, s, 1)
          'S'
          >>> choose(ps, s, 2)
          'O90'
          >>> choose(ps, s, 3)
          'd5p'
          >>> choose(ps, s, 4)
          'LE'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Ukq', 'dbMQhHK1U', '30RP1UdY', 'KdvbN', 'ljBPmC9H9', 'tU']
          >>> s = lambda p: p == 'KdvbN' or p == 'Ukq' or p == 'ljBPmC9H9'
          >>> choose(ps, s, 0)
          'Ukq'
          >>> choose(ps, s, 1)
          'KdvbN'
          >>> choose(ps, s, 2)
          'ljBPmC9H9'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['ejCQLlFjJJ', 'kVEFL19YZ', 'NV6F', 'Ub7QK0', 'zgp', 'MhPk5BZw', 'NTvvrJI971', 'x7GXW1D', 'tx2CUL']
          >>> s = lambda p: p == 'NTvvrJI971' or p == 'NV6F' or p == 'kVEFL19YZ' or p == 'x7GXW1D' or p == 'zgp'
          >>> choose(ps, s, 0)
          'kVEFL19YZ'
          >>> choose(ps, s, 1)
          'NV6F'
          >>> choose(ps, s, 2)
          'zgp'
          >>> choose(ps, s, 3)
          'NTvvrJI971'
          >>> choose(ps, s, 4)
          'x7GXW1D'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['t', 'ia', 'IrGh3gZ', 'TMQ0KWEaqu', 'S', 't5', 'JkkzgRT', 'R']
          >>> s = lambda p: p == 'IrGh3gZ' or p == 'R' or p == 'TMQ0KWEaqu' or p == 'ia'
          >>> choose(ps, s, 0)
          'ia'
          >>> choose(ps, s, 1)
          'IrGh3gZ'
          >>> choose(ps, s, 2)
          'TMQ0KWEaqu'
          >>> choose(ps, s, 3)
          'R'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['haAQbpI9']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['uRLyF', '5', '1StG72K2', '1Vopk', 'J7blr5gu', '48HObQ', 'ZeDZPCa']
          >>> s = lambda p: p == '1StG72K2' or p == '1Vopk' or p == 'J7blr5gu' or p == 'ZeDZPCa'
          >>> choose(ps, s, 0)
          '1StG72K2'
          >>> choose(ps, s, 1)
          '1Vopk'
          >>> choose(ps, s, 2)
          'J7blr5gu'
          >>> choose(ps, s, 3)
          'ZeDZPCa'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['xOP24D0', 'Zodm4', 'uwMG3', 'Mezx', 'Cnx']
          >>> s = lambda p: p == 'Cnx' or p == 'Zodm4' or p == 'uwMG3'
          >>> choose(ps, s, 0)
          'Zodm4'
          >>> choose(ps, s, 1)
          'uwMG3'
          >>> choose(ps, s, 2)
          'Cnx'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['uysO', 'xr', 'QlQVnYpC', '60cnCRSFpD', 'KJMpWnm', 'JtCa62c', 'pucq0LauM2']
          >>> s = lambda p: p == 'JtCa62c' or p == 'KJMpWnm' or p == 'QlQVnYpC' or p == 'pucq0LauM2'
          >>> choose(ps, s, 0)
          'QlQVnYpC'
          >>> choose(ps, s, 1)
          'KJMpWnm'
          >>> choose(ps, s, 2)
          'JtCa62c'
          >>> choose(ps, s, 3)
          'pucq0LauM2'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['kYdw', 'xZprfY0a', 'jCUQeZSTYC', 'ozip', 'fG4pdENZ', 'W79']
          >>> s = lambda p: p == 'ozip'
          >>> choose(ps, s, 0)
          'ozip'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['4U', 'XX9Q', 'dP']
          >>> s = lambda p: p == 'XX9Q'
          >>> choose(ps, s, 0)
          'XX9Q'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['dBn', 'FIUqoQH', 'Rd']
          >>> s = lambda p: p == 'FIUqoQH' or p == 'Rd' or p == 'dBn'
          >>> choose(ps, s, 0)
          'dBn'
          >>> choose(ps, s, 1)
          'FIUqoQH'
          >>> choose(ps, s, 2)
          'Rd'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['ONaaOd86', 'ieq1a']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['418oTaUHk6']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['S', 'OjBP', 'Tr6n34PS8D', 'o60Xa']
          >>> s = lambda p: p == 'OjBP' or p == 'S' or p == 'o60Xa'
          >>> choose(ps, s, 0)
          'S'
          >>> choose(ps, s, 1)
          'OjBP'
          >>> choose(ps, s, 2)
          'o60Xa'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['gZGj8G9', 'tJOJixv2E', 'Rzt', 'uSlA95Kop', 'uPNkjiUV9K', 'WjTvFY']
          >>> s = lambda p: p == 'Rzt' or p == 'uPNkjiUV9K' or p == 'uSlA95Kop'
          >>> choose(ps, s, 0)
          'Rzt'
          >>> choose(ps, s, 1)
          'uSlA95Kop'
          >>> choose(ps, s, 2)
          'uPNkjiUV9K'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['p', 'Qu', 'HWfS6W', 'Hle', 'AzhNgkwD', 'nbWO', 'qGf3vd9', 'nQ1VdUxn7Z']
          >>> s = lambda p: p == 'HWfS6W' or p == 'p' or p == 'qGf3vd9'
          >>> choose(ps, s, 0)
          'p'
          >>> choose(ps, s, 1)
          'HWfS6W'
          >>> choose(ps, s, 2)
          'qGf3vd9'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['TwRL6', 's8HA7NEy9', 'x']
          >>> s = lambda p: p == 'x'
          >>> choose(ps, s, 0)
          'x'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Ne6L', 'kGR']
          >>> s = lambda p: p == 'Ne6L'
          >>> choose(ps, s, 0)
          'Ne6L'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['D0D', 'LcCQ1']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['lgp', '6o6Hu5GB', 'I']
          >>> s = lambda p: p == '6o6Hu5GB'
          >>> choose(ps, s, 0)
          '6o6Hu5GB'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['ypHvW', '05ZvX', 'ih', 'y', '3lfSRPXYUp']
          >>> s = lambda p: p == '05ZvX' or p == 'ih' or p == 'y'
          >>> choose(ps, s, 0)
          '05ZvX'
          >>> choose(ps, s, 1)
          'ih'
          >>> choose(ps, s, 2)
          'y'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['L', 'YwD5']
          >>> s = lambda p: p == 'YwD5'
          >>> choose(ps, s, 0)
          'YwD5'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['t2fcKxcHGV', 'hcOr0', 'N7VV', 'Ktu9', '10E', 'Fi']
          >>> s = lambda p: p == 'hcOr0'
          >>> choose(ps, s, 0)
          'hcOr0'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['S0HHc29', 'VjcL88A', '9Y', '8THN']
          >>> s = lambda p: p == '9Y' or p == 'S0HHc29'
          >>> choose(ps, s, 0)
          'S0HHc29'
          >>> choose(ps, s, 1)
          '9Y'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Z1hCZfe4s9', 'uDSu', 'eJonD']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['behMPcxcjj', 'cAPdpB', 'egujs2jv', '2kEi6Y']
          >>> s = lambda p: p == 'behMPcxcjj' or p == 'cAPdpB' or p == 'egujs2jv'
          >>> choose(ps, s, 0)
          'behMPcxcjj'
          >>> choose(ps, s, 1)
          'cAPdpB'
          >>> choose(ps, s, 2)
          'egujs2jv'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['5OjO']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
