from app.models import Comment,User
from app import db

def tearDown(self):
        Comment.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.comment,'Good work')
        self.assertEquals(self.new_comment.user_id,4)
        self.assertEquals(self.new_comment.post_id,3)

 def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


if __name__ == '__main__':
    unittest.main()