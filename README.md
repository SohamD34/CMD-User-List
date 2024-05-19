# CMD-User-List
A user list with user details, accessible using command line 

## How to use and access ?

* Navigate to the desired location and clone the repository.
``` git clone https://www.github.com/SohamD34/CMD-User-List.git ```

* In CMD, navigate to the folder location
``` cd your_desired_folder/ ```

### To view the information about the webapp
``` python list.py -h  ```

### Creating a user 
``` python list.py -a --username='name' --user_id='id' --user_email='email@email.com' ```

### Viewing user list
``` python list.py -lu ```

### Viewing user emails list
``` python list.py -le ```

### Viewing user IDs list
``` python list.py -li ```

### Editing an user information
``` python list.py -ed --username='new_name' --user_id='new_id' --user_email='new_email' ```

### Deleting a user 
``` python list.py -r=index ```
