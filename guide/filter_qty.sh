#!/bin/bash

  curl -X GET \
   -H "Authorization: JWT ${TOKEN}" \
   -H "Content-Type: application/json" \
   "http://127.0.0.1:5000/qty?start=5&end=10"
