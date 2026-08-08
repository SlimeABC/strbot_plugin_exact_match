import astrbot.api.message_components as Comp
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("exact_match", "Slime", "精确匹配回复插件", "1.0.0", "")
class ExactMatchPlugin(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context)
        self.config = config or {}
        
        triggers = self.config.get("triggers", [])
        responses = self.config.get("responses", [])
        
        self.rules = []
        for i in range(min(len(triggers), len(responses))):
            self.rules.append({
                "trigger": triggers[i],
                "response": responses[i]
            })
        
        logger.info(f"精确匹配插件已加载，{len(self.rules)} 条规则")

    @filter.event_message_type(filter.EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent):
        message_chain = event.message_obj.message
        content = ""
        
        if message_chain and len(message_chain) > 0:
            first_seg = message_chain[0]
            if isinstance(first_seg, Comp.At) and str(first_seg.qq) == str(event.message_obj.self_id):
                text_parts = []
                for seg in message_chain[1:]:
                    if isinstance(seg, Comp.Plain):
                        text_parts.append(seg.text)
                content = "".join(text_parts).strip()
            else:
                content = event.message_str.strip()
        else:
            content = event.message_str.strip()
        
        if not content:
            return
        
        for rule in self.rules:
            if content == rule["trigger"]:
                yield event.plain_result(rule["response"])
                return

    async def terminate(self):
        pass
