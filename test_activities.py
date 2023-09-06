import unittest
import argparse
from unittest.mock import patch

from MyProgram import main
import BoredAPIWrapper
import ActivitiesManagement


class TestMain(unittest.TestCase):
    @patch.object(BoredAPIWrapper.BoredAPIWrapper, 'get_random_activity')
    def test_new_command(self, mock_get_random_activity):
        mock_activity = {
            'activity': 'Learn to play the guitar',
            'type': 'education',
            'participants': 1,
            'price': 0.0,
            'link': 'https://www.wikihow.com/Learn-to-Play-the-Guitar',
            'key': '32784',
            'accessibility': 0.5
        }

        mock_get_random_activity.return_value = mock_activity

        args = argparse.Namespace(
            command='new',
            type='education',
            participants='1',
            price_min='0.1',
            price_max='30',
            accessibility_min='0.1',
            accessibility_max='0.5'
        )

        activity = main(args)

        self.assertEqual(activity, mock_activity)

    @patch.object(ActivitiesManagement.ActivityDatabase, 'get_latest_activities')
    def test_list_command(self, mock_get_latest_activities):
        mock_activities = [
            ActivitiesManagement.Activity('Activity1', 'type1', 1, 0.1, 'link1', 'key1', 0.1),
            ActivitiesManagement.Activity('Activity2', 'type2', 2, 0.2, 'link2', 'key2', 0.2),
            ActivitiesManagement.Activity('Activity3', 'type3', 2, 0.2, 'link2', 'key2', 0.2),
            ActivitiesManagement.Activity('Activity4', 'type4', 2, 0.2, 'link2', 'key2', 0.2),
            ActivitiesManagement.Activity('Activity5', 'type5', 2, 0.2, 'link2', 'key2', 0.2),
        ]

        mock_get_latest_activities.return_value = mock_activities

        args = argparse.Namespace(
            command='list'
        )

        activities = main(args)

        self.assertEqual(len(activities), len(mock_activities))
        for activity in activities:
            self.assertIsInstance(activity, ActivitiesManagement.Activity)


if __name__ == '__main__':
    unittest.main()
