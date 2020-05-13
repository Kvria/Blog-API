class QuoteTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

    def test__init__(self):
        self.assertEqual(self.new_quote.id,12)
        self.assertEqual(self.new_quote.quote,'“There are only two hard things in Computer Science: cache invalidation, naming things and off-by-one errors.”')
        self.assertEqual(self.new_quote.author,'Phil Karlton')
       

if __name__ == '__main__':
    unittest.main()