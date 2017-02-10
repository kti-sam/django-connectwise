API_BOARD = {
    'id': 1,
    'name': 'Projects-2-10',
    'locationId': 1,
    'businessUnitId': 10,
    'inactive': False,
    'projectFlag': False
}

API_BOARD_LIST = [API_BOARD]

API_BOARD_STATUS_LIST = [
    {
        'id': 1,
        'name': 'New',
        'boardId': 1,
    },
    {
        'id': 2,
        'name': 'In Progress',
        'boardId': 1
    },
]

API_COMPANY = {
    "id": 2,
    "identifier": "YourCompany",
    "name": "TestCompany",
    "status": {
        "id": 1,
        "name": "Active",
        "_info": {
            "status_href": "https: //some-host.com/v4_6_release/apis/3.0/company/companies/statuses/1"
        }
    },
    "type": {
        "id": 5,
        "name": "Partner",
        "_info": {
            "type_href": "https: //some-host.com/v4_6_release/apis/3.0/company/companies/types/5"
        }
    },
    "addressLine1": None,
    "addressLine2": None,
    "city": None,
    "state": None,
    "zip": None,
    "country": None,
    "phoneNumber": "1450994900",
    "faxNumber": "",
    "website": "www.YourCompany.com",
    "territoryId": 38,
    "marketId": 23,
    "accountNumber": "",
    "defaultContact": {
        "id": 77,
        "name": "Bob Dobbs",
        "_info": {
            "contact_href": "https: //some-host.com/v4_6_release/apis/3.0/company/contacts/77"
        }
    },
    "dateAcquired": "2002-08-20T18: 04: 26Z",
    "sicCode": None,
    "parentCompany": None,
    "annualRevenue": 0.0,
    "numberOfEmployees": None,
    "ownershipType": None,
    "timeZone": {
        "id": 1,
        "name": "US Eastern",
        "_info": None
    },
    "leadSource": None,
    "leadFlag": False,
    "unsubscribeFlag": False,
    "calendarId": None,
    "userDefinedField1": None,
    "userDefinedField2": None,
    "userDefinedField3": None,
    "userDefinedField4": None,
    "userDefinedField5": None,
    "userDefinedField6": None,
    "userDefinedField7": None,
    "userDefinedField8": None,
    "userDefinedField9": None,
    "userDefinedField10": None,
    "vendorIdentifier": None,
    "taxIdentifier": None,
    "taxCode": {
        "id": 11,
        "name": "State",
        "_info": {
            "taxCode_href": "https: //some-host.com/v4_6_release/apis/3.0/finance/taxCodes/11"
        }
    },
    "billingTerms": {
        "id": 2,
        "name": "Net 10 days",
        "_info": None
    },
    "invoiceTemplate": None,
    "pricingSchedule": None,
    "companyEntityType": None,
    "billToCompany": {
        "id": 2,
        "identifier": "YourCompany",
        "name": "TestCompany",
        "_info": {
            "company_href": "https: //some-host.com/v4_6_release/apis/3.0/company/companies/2"
        }
    },
    "billingSite": None,
    "billingContact": None,
    "invoiceDeliveryMethod": {
        "id": 1,
        "name": "Mail",
        "_info": None
    },
    "invoiceToEmailAddress": None,
    "invoiceCCEmailAddress": None,
    "deletedFlag": False,
    "dateDeleted": None,
    "deletedBy": None,
    "mobileGuid": "4d48fc9e-2e9a-43a6-a85d-f1996723459f",
    "currency": None,
    "territoryManager": None,
    "_info": {
        "lastUpdated": "2015-12-24T22: 08: 22Z",
        "updatedBy": "omnicorp"
    },
    "customFields": None
}

API_COMPANY_LIST = [API_COMPANY]

API_SERVICE_TICKET = {
    'id': 69,
    'summary': 'Schedule and Execute Conversion',
    'recordType': 'ProjectTicket',
    'board': {
        'id': 1,
        'name': 'Projects-2-10',
        '_info': {
            'board_href': 'https://some-host.com/v4_6_release/apis/3.0/service/boards/1'
        }
    },
    'status': {
        'id': 1,
        'name': 'New',
        '_info': {
            'status_href': 'https://some-host.com/v4_6_release/apis/3.0/service/boards/1/statuses/1'
        }
    },
    'project': {
        'id': 5,
        'name': 'Financial System Implementation',
        '_info': {
            'project_href': 'https://some-host.com/v4_6_release/apis/3.0/project/projects/5'
        }
    },
    'phase': {
        'id': 8,
        'name': 'Solution Implementation',
        '_info': {
            'phase_href': 'https://some-host.com/v4_6_release/apis/3.0/project/projects/5/phases/8'
        }
    },
    'wbsCode': '10.2',
    'company': {
        'id': 24,
        'identifier': 'WildEagleInc',
        'name': 'Wild Eagle, Inc.',
        '_info': {
            'company_href': 'https://some-host.com/v4_6_release/apis/3.0/company/companies/24'
        }
    },
    'site': {
        'id': 28,
        'name': 'Main',
        '_info': {
            'site_href': 'https://some-host.com/v4_6_release/apis/3.0/company/companies/24/sites/28'
        }
    },
    'siteName': None,
    'addressLine1': '140 S. Village Ave.',
    'addressLine2': '8th Floor',
    'city': 'Tampa',
    'stateIdentifier': 'FL',
    'zip': '33880',
    'country': None,
    'contact': {
        'id': 70,
        'name': 'Gregg Kegle',
        '_info': {
            'contact_href': 'https://some-host.com/v4_6_release/apis/3.0/company/contacts/70'
        }
    },
    'contactName': 'Gregg Kegle',
    'contactPhoneNumber': '8135156666',
    'contactPhoneExtension': None,
    'contactEmailAddress': 'gregg.kegle@wildeagle.com',
    'type': None,
    'subType': None,
    'item': None,
    'team': None,
    'owner': None,
    'priority': {
        'id': 4,
        'name': 'Priority 3 - Normal Response',
        'sort': 6,
        '_info': {
            'priority_href': 'https://some-host.com/v4_6_release/apis/3.0/service/priorities/4',
            'image_href': 'https://some-host.com/v4_6_release/apis/3.0/service/priorities/4/image?lm=2005-05-27T14:58:21Z'
        }
    },
    'serviceLocation': {
        'id': 1,
        'name': 'On-Site',
        '_info': {
            'location_href': 'https://some-host.com/v4_6_release/apis/3.0/service/locations/1'
        }
    },
    'source': {
        'id': 2,
        'name': 'Phone',
        '_info': {
            'source_href': 'https://some-host.com/v4_6_release/apis/3.0/service/sources/2'
        }
    },
    'requiredDate': None,
    'budgetHours': None,
    'opportunity': None,
    'agreement': None,
    'severity': 'Medium',
    'impact': 'Medium',
    'externalXRef': None,
    'poNumber': None,
    'knowledgeBaseCategoryId': None,
    'knowledgeBaseSubCategoryId': None,
    'allowAllClientsPortalView': False,
    'customerUpdatedFlag': False,
    'automaticEmailContactFlag': False,
    'automaticEmailResourceFlag': False,
    'automaticEmailCcFlag': False,
    'automaticEmailCc': None,
    'contactEmailLookup': None,
    'processNotifications': None,
    'skipCallback': None,
    'closedDate': None,
    'closedBy': None,
    'closedFlag': False,
    'dateEntered': '2005-05-27T17:30:19Z',
    'enteredBy': 'User10',
    'actualHours': None,
    'approved': True,
    'subBillingMethod': None,
    'subBillingAmount': None,
    'subDateAccepted': None,
    'dateResolved': None,
    'dateResplan': None,
    'dateResponded': None,
    'resolveMinutes': 0,
    'resPlanMinutes': 0,
    'respondMinutes': 0,
    'isInSla': False,
    'knowledgeBaseLinkId': None,
    'resources': None,
    'parentTicketId': None,
    'hasChildTicket': False,
    'knowledgeBaseLinkType': None,
    'billTime': 'NoDefault',
    'billExpenses': 'Billable',
    'billProducts': 'Billable',
    'predecessorType': None,
    'predecessorId': None,
    'predecessorClosedFlag': None,
    'lagDays': None,
    'lagNonworkingDaysFlag': None,
    'estimatedStartDate': None,
    'duration': None,
    'locationId': 2,
    'businessUnitId': 10,
    'mobileGuid': 'c5882071-79ac-4149-9088-3af3196a22f7',
    'sla': None,
    '_info': {
        'lastUpdated': '2016-03-08T21:59:20Z',
        'updatedBy': 'User1',
        'activities_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/activities',
        'timeentries_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/timeentries',
        'scheduleentries_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/scheduleentries',
        'documents_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/documents',
        'products_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/products',
        'configurations_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/configurations',
        'tasks_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/tasks',
        'notes_href': 'https://some-host.com/v4_6_release/apis/3.0/service/tickets/69/notes'
    },
    'customFields': None
}

API_SERVICE_TICKET_LIST = [API_SERVICE_TICKET]

API_SERVICE_TICKET_MAP = {
    t['id']: t
    for t in API_SERVICE_TICKET_LIST
}

API_CW_VERSION = {
    'version': 'v2.0'
}

API_MEMBER = {
    'adminFlag': False,
    'allowExpensesEnteredAgainstCompaniesFlag': True,
    'allowInCellEntryOnTimeSheet': False,
    'billableForecast': 75.0,
    'calendar': None,
    'calendarSyncIntegrationFlag': False,
    'country': None,
    'dailyCapacity': 8.0,
    'daysTolerance': 1,
    'defaultDepartmentId': 10,
    'defaultEmail': 'Office',
    'defaultLocationId': 2,
    'defaultPhone': 'Office',
    'disableOnlineFlag': False,
    'enableLdapAuthenticationFlag': False,
    'enableMobileFlag': False,
    'enableMobileGpsFlag': False,
    'enterTimeAgainstCompanyFlag': True,
    'expenseApprover': {
        'id': 176,
        'identifier': 'User1',
        'name': 'Training User1',
        '_info': {
            'member_href': 'https://some-host.com/v4_6_release/apis/3.0/system/members/176'
        }
    },
    'firstName': 'Training',
    'hideMemberInDispatchPortalFlag': False,
    'hireDate': '1800-01-01T08:00:00Z',
    'homeEmail': None,
    'homeExtension': None,
    'homePhone': None,
    'hourlyCost': 0.0,
    'hourlyRate': None,
    'id': 176,
    'identifier': 'User1',
    'inactiveDate': None,
    'inactiveFlag': False,
    'includeInUtilizationReportingFlag': False,
    'lastLogin': '2017-02-07T07:37:47Z',
    'lastName': 'User1',
    'licenseClass': 'F',
    'mapiName': None,
    'middleInitial': None,
    'minimumHours': 8.0,
    'mobileEmail': None,
    'mobileExtension': None,
    'mobilePhone': None,
    'notes': '',
    'officeEmail': 'test@test.com',
    'officeExtension': None,
    'officePhone': '555-121-2121',
    'projectDefaultBoard': None,
    'projectDefaultDepartmentId': None,
    'projectDefaultLocationId': None,
    'reportsTo': None,
    'requireExpenseEntryFlag': False,
    'requireStartAndEndTimeOnTimeEntryFlag': False,
    'requireTimeSheetEntryFlag': False,
    'restrictDefaultSalesTerritoryFlag': False,
    'restrictDefaultWarehouseBinFlag': False,
    'restrictDefaultWarehouseFlag': False,
    'restrictDepartmentFlag': False,
    'restrictLocationFlag': False,
    'restrictProjectDefaultDepartmentFlag': False,
    'restrictProjectDefaultLocationFlag': False,
    'restrictScheduleFlag': False,
    'restrictServiceDefaultDepartmentFlag': False,
    'restrictServiceDefaultLocationFlag': False,
    'salesDefaultLocationId': 39,
    'scheduleCapacity': 8.0,
    'scheduleDefaultDepartmentId': 10,
    'scheduleDefaultLocationId': 2,
    'securityLevel': 'Corporate',
    'securityLocationId': 38,
    'securityRole': {
        'id': 63,
        'name': 'Admin',
        '_info': None
    },
    'serviceDefaultBoard': {
        'id': 1,
        'name': 'Tampa Office/Services',
        '_info': {
            'board_href': 'https://some-host.com/v4_6_release/apis/3.0/service/boards/1'
        }
    },
    'serviceDefaultDepartmentId': 10,
    'serviceDefaultLocationId': 2,
    'serviceLocation': None,
    'serviceTeams': [
        25,
        26,
        28
    ],
    'timeApprover': {
        'id': 176,
        'identifier': 'User1',
        'name': 'Training User1',
        '_info': {
            'member_href': 'https://some-host.com/v4_6_release/apis/3.0/system/members/176'
        }
    },
    'timeReminderEmailFlag': False,
    'timeSheetStartDate': '2009-04-16T07:00:00Z',
    'timeZone': {
        'id': 4,
        'name': 'US Pacific',
        '_info': None
    },
    'title': None,
    'type': None,
    'vendorNumber': None,
    'warehouse': None,
    'warehouseBin': None,
    'workRole': {
        'id': 11,
        'name': 'System Engineer',
        '_info': None
    },
    'workType': None,
    '_info': {
        'lastUpdated': '2015-08-24T19:50:10Z',
        'updatedBy': 'User1',
        'image_href': 'https://some-host.com/v4_6_release/apis/3.0/system/members/176/image?lastModified=2015-08-24T19:50:10Z'
    }
}

API_MEMBER_LIST = [API_MEMBER]

API_MEMBER_COUNT = {
    'count': len(API_MEMBER_LIST)
}

API_PROJECTS = {}