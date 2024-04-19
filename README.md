# Greg Examples

Repo with example bots on different branches

## Invalid Flow

To duplicate, enter the followign in the bot:

```yml
test_cases:
  - test_case: 30c0caaf300e4c5d8669c898615322f1
    steps:
    - user: tell me about contacts
    - utter: utter_menu
    - user: List Contacts
    - utter: utter_ask_remove_contact_handle
    - user: @greg
    - utter: utter_ask_remove_contact_handle
```

- It will repeatedly ask for the contact handle
- debug log will show `ERROR    rasa.dialogue_understanding.generator.command_generator  - [error    ] command_generator.predict.error error=Invalid flow ID 'list_contacts'.`
