"""Triggers Custom Events to Responsys
"""


class EventTarget(object):
    TARGET_NODE_ENROLLMENTS = [
        'ND001', 'ND002', 'ND003',
        'ND004', 'ND005', 'ND006',
        'ND007', 'ND008', 'ND009'
    ]

    def __init__(self, data):
        self.data = data

    def validateEventType(self):
        for item in self.data:
            record = item['recordData']['records'][0]
            if record in self.TARGET_NODE_ENROLLMENTS:
                print record
