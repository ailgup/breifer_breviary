var scheme = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "additionalProperties": true,
    "title": "Hour",
    "definitions": {
        "comment": {
            "title": "Comment:",
            "type": "string",
            "format": "textarea",
            "default": ""
        },
        "yesno": {
            "default": "yes",
            "type": "string",
            "enum": [
                "yes",
                "no"
            ]
        }
    },
    "type": "object",
    "id": "https://niebert.github.io/json-editor",
    "options": {
        "disable_collapse": false,
        "disable_edit_json": false,
        "disable_properties": false,
        "collapsed": false,
        "hidden": false
    },
    "defaultProperties": [
        "invitatory",
        "psalms",
        "reading",
        "response",
        "canticle_ant",
        "intercessions",
        "prayer"
    ],
    "properties": {
        "invitatory": {
            "type": "array",
            "id": "/properties/invitatory",
            "title": "Invitatory",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "type": "object",
                "id": "/properties/invitatory/items",
                "title": "Title Root Invitatory ",
                "options": {
                    "disable_collapse": false,
                    "disable_edit_json": false,
                    "disable_properties": false,
                    "collapsed": false,
                    "hidden": false
                },
                "defaultProperties": [
                    "title",
                    "ant"
                ],
                "properties": {
                    "title": {
                        "type": "string",
                        "id": "/properties/invitatory/items/properties/title",
                        "title": "Title",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'title' Type: 'string' Path: '/properties/invitatory/items/properties/title'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 10
                    },
                    "ant": {
                        "type": "string",
                        "id": "/properties/invitatory/items/properties/ant",
                        "title": "Ant",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'ant' Type: 'string' Path: '/properties/invitatory/items/properties/ant'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 20
                    }
                }
            },
            "propertyOrder": 10
        },
        "psalms": {
            "type": "array",
            "id": "/properties/psalms",
            "title": "Psalms",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "headerTemplate": "Psalms {{i1}}",
                "oneOf": [
                    {
                        "type": "object",
                        "id": "/properties/psalms/oneof0",
                        "title": "oneof 0 /properties/psalms",
                        "options": {
                            "disable_collapse": false,
                            "disable_edit_json": false,
                            "disable_properties": false,
                            "collapsed": false,
                            "hidden": false
                        },
                        "defaultProperties": [
                            "ps_num",
                            "antiphon",
                            "psalm"
                        ],
                        "properties": {
                            "ps_num": {
                                "type": "integer",
                                "id": "/properties/psalms/items/properties/ps_num",
                                "title": "Ps Num",
                                "default": 1,
                                "description": "A description for 'ps_num'  Type: 'integer'",
                                "options": {
                                    "hidden": false
                                },
                                "propertyOrder": 10
                            },
                            "antiphon": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/antiphon",
                                "title": "Antiphon",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "headerTemplate": "Antiphon {{i1}}",
                                    "oneOf": [
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof0",
                                            "title": "oneof 0 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof1",
                                            "title": "oneof 1 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof2",
                                            "title": "oneof 2 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof3",
                                            "title": "oneof 3 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        }
                                    ]
                                },
                                "propertyOrder": 20
                            },
                            "psalm": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/psalm",
                                "title": "Psalm",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "type": "object",
                                    "id": "/properties/psalms/items/properties/psalm/items",
                                    "title": "Title Root Psalms Psalm ",
                                    "options": {
                                        "disable_collapse": false,
                                        "disable_edit_json": false,
                                        "disable_properties": false,
                                        "collapsed": false,
                                        "hidden": false
                                    },
                                    "defaultProperties": [
                                        "titles",
                                        "verse",
                                        "summary",
                                        "summary_verse",
                                        "text"
                                    ],
                                    "properties": {
                                        "titles": {
                                            "type": "array",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/titles",
                                            "title": "Titles",
                                            "format": "tabs",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_array_add": false,
                                                "disable_array_delete": false,
                                                "disable_array_reorder": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "items": {
                                                "type": "string",
                                                "id": "/properties/psalms/items/properties/psalm/items/properties/titles/items",
                                                "title": "Title Root Psalms Psalm Titles ",
                                                "default": "",
                                                "format": "text",
                                                "description": "Description for 'items' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/titles/items'",
                                                "options": {
                                                    "hidden": false
                                                }
                                            },
                                            "propertyOrder": 10
                                        },
                                        "verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/verse",
                                            "title": "Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 20
                                        },
                                        "summary": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary",
                                            "title": "Summary",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 30
                                        },
                                        "summary_verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary_verse",
                                            "title": "Summary Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary_verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary_verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 40
                                        },
                                        "text": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/text",
                                            "title": "Text",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'text' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/text'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 50
                                        }
                                    }
                                },
                                "propertyOrder": 30
                            }
                        }
                    },
                    {
                        "type": "object",
                        "id": "/properties/psalms/oneof1",
                        "title": "oneof 1 /properties/psalms",
                        "options": {
                            "disable_collapse": false,
                            "disable_edit_json": false,
                            "disable_properties": false,
                            "collapsed": false,
                            "hidden": false
                        },
                        "defaultProperties": [
                            "ps_num",
                            "antiphon",
                            "psalm"
                        ],
                        "properties": {
                            "ps_num": {
                                "type": "integer",
                                "id": "/properties/psalms/items/properties/ps_num",
                                "title": "Ps Num",
                                "default": 2,
                                "description": "A description for 'ps_num'  Type: 'integer'",
                                "options": {
                                    "hidden": false
                                },
                                "propertyOrder": 10
                            },
                            "antiphon": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/antiphon",
                                "title": "Antiphon",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "headerTemplate": "Antiphon {{i1}}",
                                    "oneOf": [
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof0",
                                            "title": "oneof 0 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof1",
                                            "title": "oneof 1 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof2",
                                            "title": "oneof 2 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof3",
                                            "title": "oneof 3 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        }
                                    ]
                                },
                                "propertyOrder": 20
                            },
                            "psalm": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/psalm",
                                "title": "Psalm",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "type": "object",
                                    "id": "/properties/psalms/items/properties/psalm/items",
                                    "title": "Title Root Psalms Psalm ",
                                    "options": {
                                        "disable_collapse": false,
                                        "disable_edit_json": false,
                                        "disable_properties": false,
                                        "collapsed": false,
                                        "hidden": false
                                    },
                                    "defaultProperties": [
                                        "titles",
                                        "verse",
                                        "summary",
                                        "summary_verse",
                                        "text"
                                    ],
                                    "properties": {
                                        "titles": {
                                            "type": "array",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/titles",
                                            "title": "Titles",
                                            "format": "tabs",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_array_add": false,
                                                "disable_array_delete": false,
                                                "disable_array_reorder": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "items": {
                                                "type": "string",
                                                "id": "/properties/psalms/items/properties/psalm/items/properties/titles/items",
                                                "title": "Title Root Psalms Psalm Titles ",
                                                "default": "",
                                                "format": "text",
                                                "description": "Description for 'items' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/titles/items'",
                                                "options": {
                                                    "hidden": false
                                                }
                                            },
                                            "propertyOrder": 10
                                        },
                                        "verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/verse",
                                            "title": "Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 20
                                        },
                                        "summary": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary",
                                            "title": "Summary",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 30
                                        },
                                        "summary_verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary_verse",
                                            "title": "Summary Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary_verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary_verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 40
                                        },
                                        "text": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/text",
                                            "title": "Text",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'text' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/text'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 50
                                        }
                                    }
                                },
                                "propertyOrder": 30
                            }
                        }
                    },
                    {
                        "type": "object",
                        "id": "/properties/psalms/oneof2",
                        "title": "oneof 2 /properties/psalms",
                        "options": {
                            "disable_collapse": false,
                            "disable_edit_json": false,
                            "disable_properties": false,
                            "collapsed": false,
                            "hidden": false
                        },
                        "defaultProperties": [
                            "ps_num",
                            "antiphon",
                            "psalm"
                        ],
                        "properties": {
                            "ps_num": {
                                "type": "integer",
                                "id": "/properties/psalms/items/properties/ps_num",
                                "title": "Ps Num",
                                "default": 3,
                                "description": "A description for 'ps_num'  Type: 'integer'",
                                "options": {
                                    "hidden": false
                                },
                                "propertyOrder": 10
                            },
                            "antiphon": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/antiphon",
                                "title": "Antiphon",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "headerTemplate": "Antiphon {{i1}}",
                                    "oneOf": [
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof0",
                                            "title": "oneof 0 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof1",
                                            "title": "oneof 1 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof2",
                                            "title": "oneof 2 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        },
                                        {
                                            "type": "object",
                                            "id": "/properties/psalms/items/properties/antiphon/oneof3",
                                            "title": "oneof 3 /properties/psalms/items/properties/antiphon",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_edit_json": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "defaultProperties": [
                                                "title",
                                                "ant"
                                            ],
                                            "properties": {
                                                "title": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                                                    "title": "Title",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'title' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/title'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 10
                                                },
                                                "ant": {
                                                    "type": "string",
                                                    "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                                                    "title": "Ant",
                                                    "default": "",
                                                    "format": "text",
                                                    "description": "Description for 'ant' Type: 'string' Path: '/properties/psalms/items/properties/antiphon/items/properties/ant'",
                                                    "options": {
                                                        "hidden": false
                                                    },
                                                    "propertyOrder": 20
                                                }
                                            }
                                        }
                                    ]
                                },
                                "propertyOrder": 20
                            },
                            "psalm": {
                                "type": "array",
                                "id": "/properties/psalms/items/properties/psalm",
                                "title": "Psalm",
                                "format": "tabs",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_array_add": false,
                                    "disable_array_delete": false,
                                    "disable_array_reorder": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "items": {
                                    "type": "object",
                                    "id": "/properties/psalms/items/properties/psalm/items",
                                    "title": "Title Root Psalms Psalm ",
                                    "options": {
                                        "disable_collapse": false,
                                        "disable_edit_json": false,
                                        "disable_properties": false,
                                        "collapsed": false,
                                        "hidden": false
                                    },
                                    "defaultProperties": [
                                        "titles",
                                        "verse",
                                        "summary",
                                        "summary_verse",
                                        "text"
                                    ],
                                    "properties": {
                                        "titles": {
                                            "type": "array",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/titles",
                                            "title": "Titles",
                                            "format": "tabs",
                                            "options": {
                                                "disable_collapse": false,
                                                "disable_array_add": false,
                                                "disable_array_delete": false,
                                                "disable_array_reorder": false,
                                                "disable_properties": false,
                                                "collapsed": false,
                                                "hidden": false
                                            },
                                            "items": {
                                                "headerTemplate": "Titles {{i1}}",
                                                "oneOf": [
                                                    {
                                                        "type": "string",
                                                        "id": "/properties/psalms/items/properties/psalm/items/properties/titles/oneof0",
                                                        "title": "oneof 0 /properties/psalms/items/properties/psalm/items/properties/titles",
                                                        "default": "",
                                                        "format": "text",
                                                        "description": "Description for 'items' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/titles/items'",
                                                        "options": {
                                                            "hidden": false
                                                        }
                                                    },
                                                    {
                                                        "type": "string",
                                                        "id": "/properties/psalms/items/properties/psalm/items/properties/titles/oneof1",
                                                        "title": "oneof 1 /properties/psalms/items/properties/psalm/items/properties/titles",
                                                        "default": "",
                                                        "format": "text",
                                                        "description": "Description for 'items' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/titles/items'",
                                                        "options": {
                                                            "hidden": false
                                                        }
                                                    }
                                                ]
                                            },
                                            "propertyOrder": 10
                                        },
                                        "verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/verse",
                                            "title": "Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 20
                                        },
                                        "summary": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary",
                                            "title": "Summary",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 30
                                        },
                                        "summary_verse": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/summary_verse",
                                            "title": "Summary Verse",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'summary_verse' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/summary_verse'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 40
                                        },
                                        "text": {
                                            "type": "string",
                                            "id": "/properties/psalms/items/properties/psalm/items/properties/text",
                                            "title": "Text",
                                            "default": "",
                                            "format": "text",
                                            "description": "Description for 'text' Type: 'string' Path: '/properties/psalms/items/properties/psalm/items/properties/text'",
                                            "options": {
                                                "hidden": false
                                            },
                                            "propertyOrder": 50
                                        }
                                    }
                                },
                                "propertyOrder": 30
                            }
                        }
                    }
                ]
            },
            "propertyOrder": 20
        },
        "reading": {
            "type": "array",
            "id": "/properties/reading",
            "title": "Reading",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "type": "object",
                "id": "/properties/reading/items",
                "title": "Title Root Reading ",
                "options": {
                    "disable_collapse": false,
                    "disable_edit_json": false,
                    "disable_properties": false,
                    "collapsed": false,
                    "hidden": false
                },
                "defaultProperties": [
                    "verse",
                    "text"
                ],
                "properties": {
                    "verse": {
                        "type": "string",
                        "id": "/properties/reading/items/properties/verse",
                        "title": "Verse",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'verse' Type: 'string' Path: '/properties/reading/items/properties/verse'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 10
                    },
                    "text": {
                        "type": "string",
                        "id": "/properties/reading/items/properties/text",
                        "title": "Text",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'text' Type: 'string' Path: '/properties/reading/items/properties/text'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 20
                    }
                }
            },
            "propertyOrder": 30
        },
        "response": {
            "type": "array",
            "id": "/properties/response",
            "title": "Response",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "type": "array",
                "id": "/properties/response/items",
                "title": "Title Root Response ",
                "format": "tabs",
                "options": {
                    "disable_collapse": false,
                    "disable_array_add": false,
                    "disable_array_delete": false,
                    "disable_array_reorder": false,
                    "disable_properties": false,
                    "collapsed": false,
                    "hidden": false
                },
                "items": {
                    "headerTemplate": "Title Root Response  {{i1}}",
                    "oneOf": [
                        {
                            "type": "object",
                            "id": "/properties/response/items/oneof0",
                            "title": "oneof 0 /properties/response/items",
                            "options": {
                                "disable_collapse": false,
                                "disable_edit_json": false,
                                "disable_properties": false,
                                "collapsed": false,
                                "hidden": false
                            },
                            "defaultProperties": [
                                "verse",
                                "response"
                            ],
                            "properties": {
                                "verse": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/verse",
                                    "title": "Verse",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'verse' Type: 'string' Path: '/properties/response/items/items/properties/verse'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 10
                                },
                                "response": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/response",
                                    "title": "Response",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'response' Type: 'string' Path: '/properties/response/items/items/properties/response'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 20
                                }
                            }
                        },
                        {
                            "type": "object",
                            "id": "/properties/response/items/oneof1",
                            "title": "oneof 1 /properties/response/items",
                            "options": {
                                "disable_collapse": false,
                                "disable_edit_json": false,
                                "disable_properties": false,
                                "collapsed": false,
                                "hidden": false
                            },
                            "defaultProperties": [
                                "verse",
                                "response"
                            ],
                            "properties": {
                                "verse": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/verse",
                                    "title": "Verse",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'verse' Type: 'string' Path: '/properties/response/items/items/properties/verse'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 10
                                },
                                "response": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/response",
                                    "title": "Response",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'response' Type: 'string' Path: '/properties/response/items/items/properties/response'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 20
                                }
                            }
                        },
                        {
                            "type": "object",
                            "id": "/properties/response/items/oneof2",
                            "title": "oneof 2 /properties/response/items",
                            "options": {
                                "disable_collapse": false,
                                "disable_edit_json": false,
                                "disable_properties": false,
                                "collapsed": false,
                                "hidden": false
                            },
                            "defaultProperties": [
                                "verse",
                                "response"
                            ],
                            "properties": {
                                "verse": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/verse",
                                    "title": "Verse",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'verse' Type: 'string' Path: '/properties/response/items/items/properties/verse'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 10
                                },
                                "response": {
                                    "type": "string",
                                    "id": "/properties/response/items/items/properties/response",
                                    "title": "Response",
                                    "default": "",
                                    "format": "text",
                                    "description": "Description for 'response' Type: 'string' Path: '/properties/response/items/items/properties/response'",
                                    "options": {
                                        "hidden": false
                                    },
                                    "propertyOrder": 20
                                }
                            }
                        }
                    ]
                }
            },
            "propertyOrder": 40
        },
        "canticle_ant": {
            "type": "array",
            "id": "/properties/canticle_ant",
            "title": "Canticle Ant",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "type": "object",
                "id": "/properties/canticle_ant/items",
                "title": "Title Root Canticle Ant ",
                "options": {
                    "disable_collapse": false,
                    "disable_edit_json": false,
                    "disable_properties": false,
                    "collapsed": false,
                    "hidden": false
                },
                "defaultProperties": [
                    "title",
                    "ant"
                ],
                "properties": {
                    "title": {
                        "type": "string",
                        "id": "/properties/canticle_ant/items/properties/title",
                        "title": "Title",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'title' Type: 'string' Path: '/properties/canticle_ant/items/properties/title'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 10
                    },
                    "ant": {
                        "type": "string",
                        "id": "/properties/canticle_ant/items/properties/ant",
                        "title": "Ant",
                        "default": "",
                        "format": "text",
                        "description": "Description for 'ant' Type: 'string' Path: '/properties/canticle_ant/items/properties/ant'",
                        "options": {
                            "hidden": false
                        },
                        "propertyOrder": 20
                    }
                }
            },
            "propertyOrder": 50
        },
        "intercessions": {
            "type": "object",
            "id": "/properties/intercessions",
            "title": "Intercessions",
            "options": {
                "disable_collapse": false,
                "disable_edit_json": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "defaultProperties": [
                "first",
                "response",
                "intercessions"
            ],
            "properties": {
                "first": {
                    "type": "string",
                    "id": "/properties/intercessions/properties/first",
                    "title": "First",
                    "default": "",
                    "format": "text",
                    "description": "Description for 'first' Type: 'string' Path: '/properties/intercessions/properties/first'",
                    "options": {
                        "hidden": false
                    },
                    "propertyOrder": 10
                },
                "response": {
                    "type": "string",
                    "id": "/properties/intercessions/properties/response",
                    "title": "Response",
                    "default": "",
                    "format": "text",
                    "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/response'",
                    "options": {
                        "hidden": false
                    },
                    "propertyOrder": 20
                },
                "intercessions": {
                    "type": "array",
                    "id": "/properties/intercessions/properties/intercessions",
                    "title": "Intercessions",
                    "format": "tabs",
                    "options": {
                        "disable_collapse": false,
                        "disable_array_add": false,
                        "disable_array_delete": false,
                        "disable_array_reorder": false,
                        "disable_properties": false,
                        "collapsed": false,
                        "hidden": false
                    },
                    "items": {
                        "headerTemplate": "Intercessions {{i1}}",
                        "oneOf": [
                            {
                                "type": "object",
                                "id": "/properties/intercessions/properties/intercessions/oneof0",
                                "title": "oneof 0 /properties/intercessions/properties/intercessions",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_edit_json": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "defaultProperties": [
                                    "verse",
                                    "response"
                                ],
                                "properties": {
                                    "verse": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/verse",
                                        "title": "Verse",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'verse' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/verse'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 10
                                    },
                                    "response": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/response",
                                        "title": "Response",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/response'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 20
                                    }
                                }
                            },
                            {
                                "type": "object",
                                "id": "/properties/intercessions/properties/intercessions/oneof1",
                                "title": "oneof 1 /properties/intercessions/properties/intercessions",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_edit_json": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "defaultProperties": [
                                    "verse",
                                    "response"
                                ],
                                "properties": {
                                    "verse": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/verse",
                                        "title": "Verse",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'verse' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/verse'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 10
                                    },
                                    "response": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/response",
                                        "title": "Response",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/response'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 20
                                    }
                                }
                            },
                            {
                                "type": "object",
                                "id": "/properties/intercessions/properties/intercessions/oneof2",
                                "title": "oneof 2 /properties/intercessions/properties/intercessions",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_edit_json": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "defaultProperties": [
                                    "verse",
                                    "response"
                                ],
                                "properties": {
                                    "verse": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/verse",
                                        "title": "Verse",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'verse' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/verse'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 10
                                    },
                                    "response": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/response",
                                        "title": "Response",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/response'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 20
                                    }
                                }
                            },
                            {
                                "type": "object",
                                "id": "/properties/intercessions/properties/intercessions/oneof3",
                                "title": "oneof 3 /properties/intercessions/properties/intercessions",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_edit_json": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "defaultProperties": [
                                    "verse",
                                    "response"
                                ],
                                "properties": {
                                    "verse": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/verse",
                                        "title": "Verse",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'verse' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/verse'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 10
                                    },
                                    "response": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/response",
                                        "title": "Response",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/response'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 20
                                    }
                                }
                            },
                            {
                                "type": "object",
                                "id": "/properties/intercessions/properties/intercessions/oneof4",
                                "title": "oneof 4 /properties/intercessions/properties/intercessions",
                                "options": {
                                    "disable_collapse": false,
                                    "disable_edit_json": false,
                                    "disable_properties": false,
                                    "collapsed": false,
                                    "hidden": false
                                },
                                "defaultProperties": [
                                    "verse",
                                    "response"
                                ],
                                "properties": {
                                    "verse": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/verse",
                                        "title": "Verse",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'verse' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/verse'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 10
                                    },
                                    "response": {
                                        "type": "string",
                                        "id": "/properties/intercessions/properties/intercessions/items/properties/response",
                                        "title": "Response",
                                        "default": "",
                                        "format": "text",
                                        "description": "Description for 'response' Type: 'string' Path: '/properties/intercessions/properties/intercessions/items/properties/response'",
                                        "options": {
                                            "hidden": false
                                        },
                                        "propertyOrder": 20
                                    }
                                }
                            }
                        ]
                    },
                    "propertyOrder": 30
                }
            },
            "propertyOrder": 60
        },
        "prayer": {
            "type": "array",
            "id": "/properties/prayer",
            "title": "Prayer",
            "format": "tabs",
            "options": {
                "disable_collapse": false,
                "disable_array_add": false,
                "disable_array_delete": false,
                "disable_array_reorder": false,
                "disable_properties": false,
                "collapsed": false,
                "hidden": false
            },
            "items": {
                "type": "string",
                "id": "/properties/prayer/items",
                "title": "Title Root Prayer ",
                "default": "",
                "format": "text",
                "description": "Description for 'items' Type: 'string' Path: '/properties/prayer/items'",
                "options": {
                    "hidden": false
                }
            },
            "propertyOrder": 70
        }
    }
}