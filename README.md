# Assignment 3: MessageQueue (Radomir Roman & Dhamrik Chaklasiya)

we are using Fast API because FastAPI is a Python framework and set of tools that enables developers to use a REST interface to call commonly used functions to implement applications. It is accessed through a REST API to call common building blocks for an app.


### API
Using fast API running on port 7500
- overview of endpoints is at http://localhost:7500/docs
- POST method to create queues if the queue exists and if not then create the queue and push jobs into the jobs queues as well. 
- PUT for pulling jobs from queues method will also follow the same process as the Post method but this time for retrieving jobs from queues. 
- DELETE method will just check authentication and delete a queue if it exists 
- GET method will also check authentication and retrieve the full list of all queues 
- Log is stored in *logging.log*

### Config
- in configuration file *config.py* there is a variable *max_num_of_messages_per_queue* for configuring the maximum number of messages in a given queue.

### Miscellaneous
- all the packages nescessary to use the api are stored in *requirements.txt*