from modules.listener import Listener
from modules.speaker import Speaker
from modules.functions import Functions

speaker = Speaker()
listener = Listener()
fn = Functions()

fn.greet()
data = listener.passive_listen()

