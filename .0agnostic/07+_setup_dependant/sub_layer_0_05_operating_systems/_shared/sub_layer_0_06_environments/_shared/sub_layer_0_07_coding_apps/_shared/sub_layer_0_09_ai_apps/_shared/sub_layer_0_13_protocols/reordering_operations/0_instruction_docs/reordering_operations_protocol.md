---
resource_id: "0142bb34-db85-4c6a-9d17-809709dd461e"
resource_type: "document"
resource_name: "reordering_operations_protocol"
---
# Reordering Operations Protocol

<!-- section_id: "8e0b2e98-1df4-4722-aed2-c910f53b42e0" -->
## Applicability
**Context:** Use this protocol whenever you need to reorder numbered items in the context system (sub-layers, stages, protocol folders, etc.).  
**Scope:** OS: universal; Tools: universal – applies to any reordering operation within the layered context system, regardless of OS or AI coding tool.  
**Triggers:**  
- User requests to change the order of sub-layers (e.g., "make universal_protocols come after universal_tools").  
- User requests to change the order of stages within a layer.  
- User requests to change the order of any numbered items in the system.  
- Any operation that requires renaming numbered folders/files to reflect a new ordering.

---

<!-- section_id: "1d490f4f-88dd-4ff7-b5f0-dfbb4f2296a3" -->
## 1. Pre-Operation: Load Required Context

**Before performing any reordering operation, you MUST load the following context:**

<!-- section_id: "8632969a-271e-4ee2-b22a-886e771ac3c3" -->
### 1.1 For Sub-Layer Reordering

1. **Read the Sub-Layer Registry System:**
   - `layer_0/0.02_sub_layers/0.00_sub_layer_registry/README.md`
   - This explains the stable slug system and why numeric ordering can change.

2. **Read the Registry Script Documentation:**
   - `layer_0/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py`
   - Understand how the registry generation works.

3. **Check Current Registry State:**
   - `layer_0/0.02_sub_layers/0.00_sub_layer_registry/sub_layer_registry.yaml`
   - This shows the current numbering and slugs.

4. **Review Universal Init Prompt for Reordering Guidance:**
   - `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md`
   - Section 1.2 "Context Change Protocol (Ordering / Naming)" contains detailed reordering steps.

<!-- section_id: "c93a6403-0cc0-4cbd-9db5-cc62938e1f1d" -->
### 1.2 For Stage Reordering

1. **Read the Layer/Stage Framework:**
   - `0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
   - Understand how stages are numbered and organized.

2. **Check Current Stage Structure:**
   - Review the `0.99_stages/` folder in the relevant layer to see current stage numbering.

<!-- section_id: "d0e5d13c-5781-412f-aca3-e4d776d18582" -->
### 1.3 For Other Numbered Item Reordering

1. **Identify the registry/index system** (if any) for the items being reordered.
2. **Load documentation** explaining the numbering scheme and any automation scripts.

---

<!-- section_id: "8d7c061c-657e-4b25-81f6-d2d968e09839" -->
## 2. Reordering Steps

<!-- section_id: "9b9fb5af-be47-4076-ac12-72416625e6d3" -->
### 2.1 Sub-Layer Reordering

**Step 1: Understand the Request**
- Identify which sub-layers need to be reordered.
- Determine the desired final order.
- Note: The **slug** (e.g., `universal_protocols`) is the stable identifier; the number (e.g., `0.13`) is just ordering.

**Step 2: Rename Folders**
- Use temporary high numbers (e.g., `0.99_`) to avoid conflicts when swapping.
- Example: To swap `0.06_environment_setup` and `0.07_coding_app_setup`:
  ```bash
  mv sub_layer_0_06_environment_setup sub_layer_0_99_environment_setup
  mv sub_layer_0_07_coding_app_setup sub_layer_0_06_coding_app_setup
  mv sub_layer_0_99_environment_setup sub_layer_0_07_environment_setup
  ```

**Step 3: Regenerate Registry and Aliases**
- **CRITICAL:** After renaming, you MUST regenerate the registry:
  ```bash
  cd <universal_context_root>/0_context
  python3 layer_0/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py generate
  ```

**Step 4: Verify Changes**
- Check that `sub_layer_registry.yaml` reflects the new numbering.
- Verify that alias files in `aliases/` still point to the correct folders.
- Test that any hard-linked references still work (or note that they need updating).

**Step 5: Check for Hard-Linked References (Optional but Recommended)**
- Run the check script to find docs that still use numeric paths:
  ```bash
  python3 layer_0/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py check-hardlinks
  ```
- Update any critical hard-linked references to use alias paths instead.

<!-- section_id: "9c1025a8-cad8-4b70-af03-9db3cf2bb43f" -->
### 2.2 Stage Reordering

**Step 1: Understand the Request**
- Identify which stages need to be reordered.
- Determine the desired final order.

**Step 2: Rename Stage Folders**
- Use temporary high numbers to avoid conflicts.
- Example: To swap `stage_0_03_instructions` and `stage_0_04_planning`:
  ```bash
  mv stage_0_03_instructions stage_0_99_instructions
  mv stage_0_04_planning stage_0_01_planning
  mv stage_0_99_instructions stage_0_02_instructions
  ```

**Step 3: Update Status Files**
- If there's a `status_*.json` file tracking current stage, update it if needed.
- Update any documentation that references stage numbers.

**Step 4: Verify Changes**
- Check that stage folders are in the correct order.
- Verify that any stage-dependent logic still works.

<!-- section_id: "413d0787-8aa1-434c-bdf8-0a08544d2069" -->
### 2.3 Protocol Folder Reordering

**Step 1: Understand the Request**
- Identify which protocol folders need to be reordered.
- Determine the desired final order.

**Step 2: Rename Protocol Folders**
- Use temporary high numbers to avoid conflicts.
- Follow the same pattern as sub-layer reordering.

**Step 3: Update Protocol Registry/Index (if any)**
- If there's a registry or index for protocols, regenerate it.
- Update any documentation that references protocol order.

---

<!-- section_id: "6aa10d5a-ee49-489a-84eb-d70d6158b0cd" -->
## 3. Post-Operation: Verification and Documentation

<!-- section_id: "9b8a24ab-682d-4ffa-a120-ef339fb75c6c" -->
### 3.1 Verification Checklist

After any reordering operation:

- [ ] All folders/files have been renamed to reflect the new order.
- [ ] Any registries or indices have been regenerated.
- [ ] Alias files (if applicable) still point to the correct locations.
- [ ] Status files (if applicable) have been updated.
- [ ] No broken references exist (check with appropriate tools).

<!-- section_id: "27f4f862-cec9-4375-ac48-bc0dd17868c5" -->
### 3.2 Documentation Updates

- Update any README files that list the order of items.
- Update any master indices or documentation maps.
- Note any breaking changes in commit messages.

<!-- section_id: "2caa10c6-6be6-497f-ab25-707f57c41ba7" -->
### 3.3 Git Operations

After successful reordering:

1. **Stage all changes:**
   ```bash
   git add -A
   ```

2. **Commit with descriptive message:**
   ```bash
   git commit -m "Reorder [items]: [description of change, e.g., 'universal_protocols now comes after universal_tools (0.13)']"
   ```

3. **Push to remote:**
   ```bash
   git push
   ```

---

<!-- section_id: "2f05968f-b875-40ef-b278-d81cacbe692f" -->
## 4. Common Patterns and Examples

<!-- section_id: "b164cb4e-ceda-4df9-bb37-3baa292cea38" -->
### 4.1 Moving One Item After Another

**Request:** "Make X come after Y"

**Steps:**
1. Identify current numbers: X is `0.XX`, Y is `0.YY`.
2. If X > Y, move X to temporary number, then shift items between Y and X down, then move X to position after Y.
3. If X < Y, move X to temporary number, then shift items between X and Y up, then move X to position after Y.

**Example:** "Make universal_protocols come after universal_tools"
- Current: universal_tools = 0.12, universal_protocols = 0.05
- Desired: universal_tools = 0.12, universal_protocols = 0.13
- Steps:
  1. Move universal_protocols to 0.99 (temp)
  2. Move agent_setup from 0.13 to 0.14
  3. Move universal_protocols from 0.99 to 0.13
  4. Regenerate registry

<!-- section_id: "6f4c2e58-8b09-4bc2-9b94-a307d3ba1f71" -->
### 4.2 Swapping Two Adjacent Items

**Request:** "Swap X and Y"

**Steps:**
1. Move X to temporary number (e.g., 0.99)
2. Move Y to X's old number
3. Move X from temporary to Y's old number

**Example:** "Swap environment_setup and coding_app_setup"
- Current: environment_setup = 0.06, coding_app_setup = 0.07
- Steps:
  1. `mv sub_layer_0_06_environment_setup sub_layer_0_99_environment_setup`
  2. `mv sub_layer_0_07_coding_app_setup sub_layer_0_06_coding_app_setup`
  3. `mv sub_layer_0_99_environment_setup sub_layer_0_07_environment_setup`
  4. Regenerate registry

---

<!-- section_id: "569fc424-ec0a-465c-83f5-995704f35fb8" -->
## 5. Error Prevention

<!-- section_id: "c681f060-33a0-4e24-961f-1434bcfba829" -->
### 5.1 Before Starting

- **Always check current state** by reading the registry/index files.
- **Always use temporary numbers** (0.99, 0.98, etc.) to avoid conflicts.
- **Never skip the registry regeneration step** after reordering.

<!-- section_id: "01a961e0-9164-4061-b6e0-0a9ed967efd9" -->
### 5.2 During Operation

- **Work in small steps** - rename one folder at a time and verify.
- **Keep track of what you've moved** - note the old and new numbers.
- **Test as you go** - verify the structure is correct before moving to the next item.

<!-- section_id: "5e84225e-5671-4912-8098-0487c5f61e7b" -->
### 5.3 After Operation

- **Always regenerate registries/indices** - this is critical for system integrity.
- **Verify the final state** - check that everything is in the correct order.
- **Check for broken references** - use check scripts if available.

---

<!-- section_id: "575b7192-cb07-47a8-b2b2-9d70921902a7" -->
## 6. Integration with Other Protocols

This protocol works in conjunction with:

- **Protocol Writing Standard:** When documenting reordering operations, follow the protocol writing standard.
- **File Documentation Protocol:** If reordering creates new documentation needs, follow the file documentation protocol.
- **Git Commit Rule:** Always commit and push after successful reordering operations.

---

<!-- section_id: "563effdc-cd64-40ef-9944-00a243d5bfc6" -->
## 7. Troubleshooting

<!-- section_id: "ec5410e1-b25c-4e30-90cf-58bd29048bc2" -->
### Problem: Registry generation fails
- **Solution:** Check that all folder names follow the expected pattern (e.g., `sub_layer_0_XX_slug`).
- Verify that the registry script can find all sub-layer folders.

<!-- section_id: "3f42fa03-f46c-43de-a9a5-cf4a7ec957a5" -->
### Problem: Alias files point to wrong locations
- **Solution:** Regenerate the registry - alias files are auto-generated from the registry.

<!-- section_id: "d25f67d2-bf91-4f4b-bd87-f92ab15a1717" -->
### Problem: Hard-linked references break
- **Solution:** Update references to use alias paths instead of numeric paths.
- Use the `check-hardlinks` script to find all hard-linked references.

<!-- section_id: "3de345bb-7cb5-4e62-a657-64a9353a4b15" -->
### Problem: Status files show incorrect current stage
- **Solution:** Manually update status JSON files after stage reordering.
- Verify that the stage numbering in status files matches the actual folder names.

