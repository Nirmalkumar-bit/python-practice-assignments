# Task: Implement validate_payload(payload) for an API-like request body.
# Payload rules:
# - payload must be a dict else TypeError("payload must be a dict")
# - Required keys: "action", "data"
#   If missing, raise KeyError("missing key: <key>")
# - No extra keys allowed besides "action", "data", "meta"
#   If extra, raise TypeError("unexpected key: <key>")
# - action must be one of: "create", "update", "delete" else ValueError("invalid action")
# - data must be a dict else TypeError("data must be a dict")
# - For action "create": data must include non-empty str "name" and numeric "price" > 0
# - For action "update": data must include int "id" > 0 and may include "name" and/or "price" (if present, must meet same constraints)
# - For action "delete": data must include int "id" > 0 and must not include any other keys
# - meta (optional) must be a dict if provided else TypeError("meta must be a dict")
# Invalid handling messages:
# - For missing/invalid fields in data, raise ValueError with one of:
#   "invalid name", "invalid price", "invalid id", "invalid data keys"
# Expected outcome:
# - validate_payload({"action":"create","data":{"name":"Pen","price":1.5}}) returns True
# - validate_payload({"action":"delete","data":{"id":2,"name":"x"}}) raises ValueError("invalid data keys")
# - validate_payload({"action":"update","data":{"id":0}}) raises ValueError("invalid id")


def validate_payload(payload):
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dict")
    
    allowed_keys = {"action", "data", "meta"}
    required_keys = {"action", "data"}
    
    # ---- missing keys ----
    for key in required_keys:
        if key not in payload:
            raise KeyError(f"missing key: {key}")
    
    # ---- unexpected keys ----
    for key in payload:
        if key not in allowed_keys:
            raise TypeError(f"unexpected key: {key}")
    
    action = payload["action"]
    data = payload["data"]
    
    # ---- action validation ----
    if action not in ("create", "update", "delete"):
        raise ValueError("invalid action")
    
    # ---- data type ----
    if not isinstance(data, dict):
        raise TypeError("data must be a dict")
    
    # ---- meta validation ----
    if "meta" in payload and not isinstance(payload["meta"], dict):
        raise TypeError("meta must be a dict")
    
    # -------------------------
    # CREATE
    # -------------------------
    if action == "create":
        if set(data.keys()) != {"name", "price"}:
            raise ValueError("invalid data keys")
        
        name = data.get("name")
        price = data.get("price")
        
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("invalid name")
        
        if type(price) not in (int, float) or price <= 0:
            raise ValueError("invalid price")
    
    # -------------------------
    # UPDATE
    # -------------------------
    elif action == "update":
        if "id" not in data:
            raise ValueError("invalid id")
        
        allowed_update_keys = {"id", "name", "price"}
        if not set(data.keys()).issubset(allowed_update_keys):
            raise ValueError("invalid data keys")
        
        id_val = data["id"]
        if type(id_val) is not int or id_val <= 0:
            raise ValueError("invalid id")
        
        if "name" in data:
            if not isinstance(data["name"], str) or data["name"].strip() == "":
                raise ValueError("invalid name")
        
        if "price" in data:
            price = data["price"]
            if type(price) not in (int, float) or price <= 0:
                raise ValueError("invalid price")
    
    # -------------------------
    # DELETE
    # -------------------------
    elif action == "delete":
        if set(data.keys()) != {"id"}:
            raise ValueError("invalid data keys")
        
        id_val = data["id"]
        if type(id_val) is not int or id_val <= 0:
            raise ValueError("invalid id")
    
    return True


    # TODO: validate payload and return True when valid
    pass


if __name__ == "__main__":
    print(validate_payload({"action": "create", "data": {"name": "Pen", "price": 1.5}}))