from flask import jsonify, make_response, request, render_template
from flask_restful import Resource, reqparse
from pydantic import ValidationError

class ProjectRevision(Resource):
    
    def get(self, project_name, version):
        
        headers = {'Content-Type': 'text/html'}
        data = {
            'i':'{{i}}',
            'project_name': project_name.title(),
            'version': version,
            'project_description':'The Quick Brown Fox Jumps Over The Lazy Dogs',
            
            'business_domain_name':'{{self.business_domain_name}}',
            'business_domain_description': '{{self.business_domain_description}}',
        }

        return make_response(
            render_template('index.html',**data)
            , 200, headers)

class ProjectSchema(Resource):
    
    def get(self, project_name, version):
        return jsonify(
{
  "title": "Business Domain",
  "type": "object",
  "id": "business_domain",
  "properties": {
    "business_domain_name": {
      "type": "string",
      "title": "Business Domain Name",
      "minLength": 4,
      "propertyOrder":1
    },
    "business_domain_description": {
      "type": "string",
      "title": "Business Domain Description (BDD Style)",
      "format": "markdown",
      "propertyOrder":2,
      "options": {
        "ace": {
          "theme": "ace/theme/vibrant_ink",
          "tabSize": 4,
          "useSoftTabs": True,
          "wrap": True,
          "minLines":10,
          "maxLines": 20
          # "printMarginColumn": 3
        }
      }
    },
    "end_points": {
        "type": "array",
        "format": "tabs",
        "id":"end_points",
        "title": "End Points", 
        "uniqueItems": False,
        "propertyOrder":3,
        "items":{
            "title": "End Point",
            "type": "object",
            "properties": {
                "end_point_path": {
                    "id": "end_point_path",
                    "type": "string",
                    "title": "End Point Path",
                    "minLength": 4,
                    "propertyOrder":1
                },
                "model": {
                    "type": "string",
                    "template": "{{end_point_path_watch}}",
                    "watch": {
                      "end_point_path_watch": "business_domain.end_points.end_point_path"
                    }
                }
            }
        }
    },
    "age": {
      "type": "integer",
      "default": 21,
      "minimum": 18,
      "maximum": 99,
      "propertyOrder":99
    },
    "gender": {
      "type": "string",
      "enum": [
        "male",
        "female"
      ],
      "propertyOrder":3
    },
    "location": {
      "type": "object",
      "title": "Location",
      "properties": {
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "citystate": {
          "type": "string",
          "description": "This is generated automatically from the previous two fields",
          "template": "{{city}}, {{state}}",
          "watch": {
            "city": "business_domain.location.city",
            "state": "business_domain.location.state"
          }
        }
      },
      "propertyOrder":4
    },
    "pets": {
      "type": "array",
      "format": "table",
      "title": "Pets",
      "uniqueItems": True,
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "cat",
              "dog",
              "bird",
              "reptile",
              "other"
            ],
            "default": "dog"
          },
          "name": {
            "type": "string"
          },
          "fixed": {
            "type": "boolean",
            "title": "spayed / neutered"
          }
        }
      }
    },
    "Response": {
      "type": "string",
      "format": "json",
      "options": {
        "ace": {
          "theme": "ace/theme/vibrant_ink",
          "tabSize": 4,
          "useSoftTabs": True,
          "wrap": True
        }
      }
    }
  }
})

    def post(self, project_name, version):
      print(project_name)
      print(version)
      print(request.json)
      return "pass"