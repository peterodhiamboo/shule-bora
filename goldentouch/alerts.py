class Messages(object):
    def __init__(self, message):
        self.message = {
            'fee_success' : ('<div class="alert alert-success" role="alert"> '
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
            '<span aria-hidden="true">&times;</span>'
            '</button>' + message + '</div>'),

            'fee_error' : ('<div class="alert alert-danger" role="alert"> '
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
            '<span aria-hidden="true">&times;</span>'
            '</button>' + message + '</div>')
        }

# first = Messages('This is an error message')
# print(first.message['fee_error'])

