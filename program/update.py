import AutoUpdate

AutoUpdate.set.url("")
AutoUpdate.set_dowload("")
AutoUpdate.set_current_version("0.1.1")

if not AutoUpdate.is_up_to_date():
    AutoUpdate.download("")
