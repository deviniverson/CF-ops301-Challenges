# Script: ADNewUser.ps1
# Author: Devin Iverson
# Date of latest revision: 05/12/2022
# Purpose: Template to quickly be able to add a user to an Active Directory

$Attributes = @{

    Enabled = $true
    ChangePasswordAtLogon = $true

    UserPrincipalName = "ferdi@GlobeXpower.com"
    Name = "Franz.Ferdinand"
    GivenName = "Franz"
    Surname = "Ferdinand"
    DisplayName = "Franz Ferdinand"
    Description = "Joined company in 2022"
    Office = "Springfield"

    Company = "GlobeX USA"
    Department = "TPS"
    Title = "TPS Reporting Lead"
    City = "Springfield"
    State = "OR"

    AccountPassword = "FakePassword123" | ConvertTo-SecureString -AsPlainText -Force
}

New-ADUser @Attributes
