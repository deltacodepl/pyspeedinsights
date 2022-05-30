import argparse

from ..conf.data import COMMAND_CHOICES, metrics_choices


def parse_args():
    """
    Parse command line arguments as parameters for the request.
    """
    parser = argparse.ArgumentParser(prog='pyspeedinsights')
    
    # Add argument options for default API call query params
    api_group = parser.add_argument_group('API Group')
    api_group.add_argument(
        "url", help="The URL of the site you want to analyze.")
    api_group.add_argument(
        "-c", "--category", metavar="\b", dest="category",
        choices=COMMAND_CHOICES['category'],
        help="The Lighthouse category to run. Defaults to Performance.")
    api_group.add_argument(
        "-l", "--locale", metavar="\b", dest="locale",
        choices=COMMAND_CHOICES['locale'],
        help="The locale used to localize formatted results. Defaults to English (US).")
    api_group.add_argument(
        "-s", "--strategy", metavar="\b", dest="strategy",
        choices=COMMAND_CHOICES['strategy'],
        help="The analysis strategy (desktop or mobile) to use. Defaults to desktop.")
    api_group.add_argument(
        "-uc", "--campaign", metavar="\b", dest="utm_campaign",                        
        help="UTM campaign name for analytics.")
    api_group.add_argument(
        "-us", "--source", metavar="\b", dest="utm_source",
        help="UTM campaign source for analytics.")
    api_group.add_argument(
        "-t", "--token", metavar="\b", dest="captcha_token",                    
        help="The captcha token passed when filling out a captcha.")
    
    # Add other argument options for how to process the API response
    proc_group = parser.add_argument_group('Processing Group')
    proc_group.add_argument(
        "-f", "--format", metavar="\b", dest="format",
        choices=['json', 'excel'],
        help="The format of the results. Specify json (default) or excel.")
    proc_group.add_argument(
        "-m", "--metrics", metavar="\b", dest="metrics",
        choices=metrics_choices, nargs="+",
        help="Specify which metric(s) you want to include in your report.\
            This only works for Excel because the json output will include everything.\
            If excluded, additional metrics will not be dumped to Excel.\
            Add the `all` argument to retrieve all available metrics."
    )
    
    args = parser.parse_args()
    
    arg_groups={}
    # Create separate namespaces for each arg group so they can easily
    # be passed to their respective classes as kwargs
    for group in parser._action_groups:
        group_dict={a.dest:getattr(args,a.dest,None) for a in group._group_actions}
        arg_groups[group.title]=argparse.Namespace(**group_dict)
    
    return arg_groups