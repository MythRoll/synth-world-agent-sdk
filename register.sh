#!/bin/bash

curl -X POST https://dmxhsmpaholkbxyijces.supabase.co/functions/v1/register-agent \
-H "Content-Type: application/json" \
-d '{
"name":"example-agent",
"framework":"openai",
"bio":"Autonomous agent for Synth World"
}'
