# Sign in to Azure (you may skip this if you're already authenticated)
Connect-AzAccount
# Set the Azure subscription context
Set-AzContext -SubscriptionName "panhx.com_azure_subscription"

# Define the resource group and VM
$resourceGroupName = "panhx.com"
$VMName = "panhx"

# Start the VM
Start-AzVM -ResourceGroupName $resourceGroupName -Name $VMName