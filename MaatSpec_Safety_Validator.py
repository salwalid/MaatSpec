import json

# Load the Safety System JSON
safety_config = {
    # (Insert the Expanded Hierarchy JSON above)
}

def validate_action(proposed_task, category):
    """
    Checks the proposed task against the safety system and
    returns the required protocol + enforcement layers.
    """
    for tier_id, details in safety_config["harness_tiered_safety_system"].items():
        for cat_name, actions in details["action_categories"].items():
            if proposed_task in actions:
                enforcement = details.get("enforcement", {})
                return {
                    "tier": tier_id,
                    "authority": details["authority"],
                    "protocol": details["safety_protocol"],
                    "enforcement_layers": enforcement.get("active_layers", []),
                    "optional_layers": enforcement.get("optional_layers", []),
                    "authorized": False if "tier_4" in tier_id or "tier_5" in tier_id else True
                }
    return {"error": "Action not found in safety registry. Denying by default."}

# Example Usage:
# result = validate_action("one_time_payments", "financial")
# print(f"Protocol: {result['protocol']}")
# print(f"Layers:   {result['enforcement_layers']}")
# print(f"Optional: {result['optional_layers']}")
