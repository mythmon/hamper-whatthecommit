from hamper.interfaces import ChatCommandPlugin, Command
import requests


class WhatTheCommit(ChatCommandPlugin):
    name = 'whatthecommit'
    api_base_url = 'http://whatthecommit.com'

    def get_commit_message(self):
        """
        Get a commit message from the 'api'.
        """
        r = requests.get('{base}/index.txt'.format(base=self.api_base_url))
        return r.text

    class WhatTheCommitCommand(Command):
        regex = 'commit'

        def command(self, bot, comm, groups):
            """
            !commit -> Suggest a commit message from whatthecommit.com
            """
            commit_message = self.plugin.get_commit_message()
            bot.reply(comm, u'{user}: {msg}', kwvars={'msg': commit_message})
