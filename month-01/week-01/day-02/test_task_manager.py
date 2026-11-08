import unittest

from task_manager import TaskAssistant

class TestTaskAssistant(unittest.TestCase):

  def setUp(self):
    self.assistant = TaskAssistant()

  def test_add_task(self):

    result = self.assistant.add_task(
      "Learn python",
      "high"
    )

    self.assertTrue(result)

  def test_invalid_priority(self):

    result = self.assistant.add_task(
      "Invalid task",
            "urgent"
    )

    self.assertFalse(result)

  def test_update_task(self):

    self.assistant.add_task("Learn python")

    result = self.assistant.update_task(
      0,
      "Learn python and Django"
    )

    self.assertTrue(result)  



  def test_complete_task(self):

    self.assistant.add_task("Learn python")

    result = self.assistant.complete_task(0)

    self.assertTrue(result)


  def test_delete_task(self):

    self.assistant.add_task("Learn python")

    result = self.assistant.delete_task(0)

    self.assertTrue(result)



  def test_get_tasks_by_priority(self):

    self.assistant.add_task("Learn python", "high")
    self.assistant.add_task("Study RAG", "medium")

    result = self.assistant.get_tasks_by_priority("high")

    self.assertEqual(
      len(result),
      1
    )

  def test_pending_task(self):

    self.assistant.add_task("Learn python")
    self.assistant.add_task("Study RAG")

    result = self.assistant.pending_task()

    self.assertEqual(
      len(result),
      2
    )


  def test_summary_task(self):

      self.assistant.add_task("Learn python")
      self.assistant.add_task("Study RAG")

      self.assistant.complete_task(0)

      result = self.assistant.summary_task()

      self.assertEqual(
        result,
        {
          "total": 2,
          "complete": 1,
          "pending": 1
        }
      )


  def test_invalid_update_index(self):
    result = self.assistant.update_task(100, "Invalid")
    self.assertFalse(result)


  def test_invalid_complete_index(self):
    result = self.assistant.complete_task(100)
    self.assertFalse(result)


  def test_invalid_delete_index(self):
    result = self.assistant.delete_task(100)
    self.assertFalse(result)


  def test_invalid_priority_filter(self):
    result = self.assistant.get_tasks_by_priority("urgent")
    self.assertEqual(result, [])
  

if __name__ == "__main__":
  unittest.main()

  # def test_task_count(self):

  #   self.assistant.add_task("Learn Python")

  #   self.assertEqual(
  #     len(self.assistant.get_task()),
  #     1
  #   )