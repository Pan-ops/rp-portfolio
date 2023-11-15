# Set the path to your SSH key file
$SSH_KEY = "C:\Users\pan_h\panhx.com\panhx_key.pem"

# Set the username and IP address of the remote server
$REMOTE_USER = "pan"
$REMOTE_IP = "20.55.69.96"

# SSH into the remote server using the specified key
ssh -i $SSH_KEY "$REMOTE_USER@$REMOTE_IP"
