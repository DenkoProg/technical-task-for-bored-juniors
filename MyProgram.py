import argparse
import BoredAPIWrapper
import ActivitiesManagement


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('command', help='The command to run.')
        parser.add_argument('--type', help='The type of activity to get.')
        parser.add_argument('--participants', help='The number of participants for the activity.')
        parser.add_argument('--price_min', help='The minimum price for the activity.')
        parser.add_argument('--price_max', help='The maximum price for the activity.')
        parser.add_argument('--accessibility_min', help='The minimum accessibility for the activity.')
        parser.add_argument('--accessibility_max', help='The maximum accessibility for the activity.')

        args = parser.parse_args()

    if args.command == 'new':
        activity = BoredAPIWrapper.BoredAPIWrapper().get_random_activity(
            type=args.type,
            participants=args.participants,
            minprice=args.price_min,
            maxprice=args.price_max,
            minaccessibility=args.accessibility_min,
            maxaccessibility=args.accessibility_max,
        )

        ActivitiesManagement.ActivityDatabase()
        ActivitiesManagement.ActivityDatabase().create_activities_table()
        ActivitiesManagement.ActivityDatabase().save_activity(
            ActivitiesManagement.Activity(activity['activity'], activity['type'], activity['participants'],
                                          activity['price'], activity['link'], activity['key'],
                                          activity['accessibility']))

        print(activity)
        return activity


    elif args.command == 'list':
        activities = ActivitiesManagement.ActivityDatabase().get_latest_activities(5)

        for activity in activities:
            print(activity.__str__())
        return activities

    else:
        print('Invalid command.')


if __name__ == '__main__':
    main()
