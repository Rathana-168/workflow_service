from enum import Enum
from typing import Any, Dict, Sequence, List
from transitions import Machine
from transitions.core import CallbacksArg, ModelParameter, StateConfig, StateIdentifier, TransitionConfig

from app.model.request import Request

class BaseMachine(Machine):
    def __init__(self,
                 model: ModelParameter | None = ...,
                 states: Sequence[StateConfig] | type[Enum] | None = ...,
                 initial: StateIdentifier | None = 'init',
                 transitions: TransitionConfig | Sequence[TransitionConfig] | None = ...,
                 send_event: bool = ...,
                 auto_transitions: bool = ...,
                 ordered_transitions: bool = ...,
                 ignore_invalid_triggers: bool | None = ...,
                 before_state_change: CallbacksArg = ...,
                 after_state_change: CallbacksArg = ...,
                 name: str = ...,
                 queued: bool = ...,
                 prepare_event: CallbacksArg = ...,
                 finalize_event: CallbacksArg = ...,
                 model_attribute: str = ...,
                 on_exception: CallbacksArg = ...,
                 **kwargs: Dict[str, Any]) -> None:
        super().__init__(model, states, initial, transitions, send_event, auto_transitions, ordered_transitions,
                         ignore_invalid_triggers, before_state_change, after_state_change, name, queued, prepare_event,
                         finalize_event, model_attribute, on_exception, **kwargs)

class BaseTransitionClass:

    def __init__(self, req):
        if isinstance(req, int):
            self.request = '' #Logice to get request object
        elif isinstance(req, Request):
            self.request = req

        # Query Get State, transition
        states, transitions = '', ''


        self._machine = BaseMachine(self, name='BaseMachine', states=states, transitions=transitions,
                                    before_state_change=['before_state_change'],
                                    after_state_change=['after_state_change'])

    def before_state_change(self):
        pass

    def after_state_change(self):
        pass
