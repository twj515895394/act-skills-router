# 共享数据契约 v2

`scene_context`: scene_id、shot_id、duration_seconds、cast、story_facts、dialogue_exact、camera_shot、locked_constraints、target_model、evidence。

`actor_profile`: character_id、stable_body_rhythm、eye_task、voice_identity、pressure_trigger、mask_crack、scene_objective、obstacle、tactic、subtext。

`beat_sheet[]`: beat_id、start_s、end_s、trigger_id、trigger_at、reaction_at、actor_id、objective、tactic、emotion_in/out、face_actions、body_actions、dialogue_exact、listener_behavior、end_state、lock_flags。

`prompt_output[]`: shot_id、visible_state_start、ordered_actions、line_exact、voice/face/body cues、visible_state_end、negative_constraints、model_notes。

`continuity_handoff[]`: actor_id、shot_id、position、eye_line、handedness、prop_state、body_orientation、emotion_carryover、voice_lock。

`qa_report`: mode(pre_generation/post_generation)、evidence、issues[] (severity, beat_id, evidence, minimal_fix, owner_module, status)。

所有时间以镜头本地秒计；跨镜头需要额外 scene/global time mapping。相同 beat_id 保持同一触发事件，任何反应时间不得早于 trigger_at。用户保留的台词必须逐字保留，不凭空添加 plot facts。标明未知，不能伪造观察。
