*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  new
    Input Credentials  kalle  kalle123
    Input  new
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input  new
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input  new
    Input Credentials  kalle  kalle12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  new
    Input Credentials  kalle  kallekal
    Output Should Contain  Password cannot only contain lower case letters
