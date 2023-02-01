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
      "format": "table",
      "options": {},
      "items": {
        "type": "object",
        "id": "/properties/invitatory/items",
        "title": "Invitatory ",
        "options": {},
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
            "description": "",
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
            "description": "",
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
      "format": "grid",
      "options": {},
      "items": {
        "type": "object",
        "id": "/properties/psalms/oneof0",
        "title": "Psalm",
        "options": {},
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
            "description": "",
            "options": {
              "hidden": false,

            },
            "propertyOrder": 10
          },
          "antiphon": {
            "type": "array",
            "id": "/properties/psalms/items/properties/antiphon",
            "title": "Antiphon",
            "format": "table",
            "options": {},
            "items": {
              "type": "object",
              "id": "/properties/psalms/items/properties/antiphon/oneof0",
              "title": "Antiphon",
              "options": {},
              "defaultProperties": [
                "title",
                "ant"
              ],
              "properties": {
                "title": {
                  "type": "string",
                  "id": "/properties/psalms/items/properties/antiphon/items/properties/title",
                  "title": "Title",
                  "default": "Ant. 1",
                  "format": "text",
                  "description": "",
                  "options": {
                    "hidden": false,

                  },
                  "propertyOrder": 10
                },
                "ant": {
                  "type": "string",
                  "id": "/properties/psalms/items/properties/antiphon/items/properties/ant",
                  "title": "Ant",
                  "default": "",
                  "format": "text",
                  "description": "",
                  "options": {
                    "hidden": false
                  },
                  "propertyOrder": 20
                }
              }

            },
            "propertyOrder": 20
          },
          "psalm": {
            "type": "array",
            "id": "/properties/psalms/items/properties/psalm",
            "title": "Psalm",
            "format": "grid-strict",
            "options": {},
            "items": {
              "type": "object",
              "id": "/properties/psalms/items/properties/psalm/items",
              "title": "Psalm",
              "options": {"grid_break": true},
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
                  "format": "table",
                  "options": {},
                  "items": {
                    "type": "string",
                    "id": "/properties/psalms/items/properties/psalm/items/properties/titles/items",
                    "title": "Title",
                    "default": "",
                    "format": "text",
                    "description": "",
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
                  "description": "",
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
                  "description": "",
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
                  "description": "",
                  "options": {
                    "hidden": false,
					 "grid_break": true
                  },
                  "propertyOrder": 40
                },
                "text": {
                  "type": "string",
                  "id": "/properties/psalms/items/properties/psalm/items/properties/text",
                  "title": "Text",
                  "default": "",
                  "format": "textarea",
                  "description": "",
                  "options": {
                    "hidden": false,
					"input_height": "5px",
					"expand_height": true
                  },
                  "propertyOrder": 50
                }
              }
            },
            "propertyOrder": 30
          }
        }

      },
      "propertyOrder": 20
    },
    "reading": {
      "type": "array",
      "id": "/properties/reading",
      "title": "Reading",
      "format": "grid",
      "options": {},
      "items": {
        "type": "object",
        "id": "/properties/reading/items",
        "title": "Reading ",
        "options": {},
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
            "description": "",
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
            "format": "textarea",
            "description": "",
            "options": {
              "hidden": false,
			  "input_height": "5px",
              "expand_height": true
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
      "format": "table",
      "options": {},
      "items": {
        "type": "object",
        "id": "/properties/response/items/oneof0",
        "title": "Response",
        "options": {},
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
            "description": "",
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
            "description": "",
            "options": {
              "hidden": false
            },
            "propertyOrder": 20
          }
        }


      },
      "propertyOrder": 40
    },
    "canticle_ant": {
      "type": "array",
      "id": "/properties/canticle_ant",
      "title": "Canticle Ant",
      "format": "table",
      "options": {},
      "items": {
        "type": "object",
        "id": "/properties/canticle_ant/items",
        "title": "Canticle Antiphon",
        "options": {},
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
            "description": "",
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
            "description": "",
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
      "options": {},
      "defaultProperties": [
        "first",
        "response",
        "intercessions"
      ],
      "properties": {
        "first": {
          "type": "string",
          "id": "/properties/intercessions/properties/first",
          "title": "First Verse",
          "default": "",
          "format": "text",
          "description": "",
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
          "description": "",
          "options": {
            "hidden": false
          },
          "propertyOrder": 20
        },
        "intercessions": {
          "type": "array",
          "id": "/properties/intercessions/properties/intercessions",
          "title": " ",
          "format": "table",
          "options": {},
          "items": {
            "headerTemplate": "Intercessions {{i1}}",

            "type": "object",
            "id": "/properties/intercessions/properties/intercessions/oneof0",
            "title": "Subsequent Intercessions",
            "options": {},
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
                "description": "",
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
                "description": "",
                "options": {
                  "hidden": false
                },
                "propertyOrder": 20
              }
            }

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
      "format": "table",
      "options": {},
      "items": {
        "type": "string",
        "id": "/properties/prayer/items",
        "title": "Prayer",
        "default": "",
        "description": "",
        "format": "textarea",
        "options": {
          "hidden": false,
          "input_height": "50px",
          "inputAttributes": {
                "style": "width: 500px"
              },
          "expand_height": true
        }
      },
      "propertyOrder": 70
    }
  }
}