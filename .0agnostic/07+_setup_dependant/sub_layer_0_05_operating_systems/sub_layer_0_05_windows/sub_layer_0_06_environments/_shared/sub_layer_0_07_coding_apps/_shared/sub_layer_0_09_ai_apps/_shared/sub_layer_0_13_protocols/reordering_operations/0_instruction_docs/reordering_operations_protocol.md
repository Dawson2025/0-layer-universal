---
resource_id: "32054644-ed38-4c12-ad85-5febdcf0ba2c"
resource_type: "document"
resource_name: "reordering_operations_protocol"
---
# Reordering Operations Protocol

<!-- section_id: "d39a10ff-fcbf-4b29-9c04-ed3b06b81a97" -->
## Applicability
**Context:** Use this protocol whenever you need to reorder numbered items in the context system (sub-layers, stages, protocol folders, etc.).  
**Scope:** OS: universal; Tools: universal – applies to any reordering operation within the layered context system, regardless of OS or AI coding tool.  
**Triggers:**  
- User requests to change the order of sub-layers (e.g., "make universal_protocols come after universal_tools").  
- User requests to change the order of stages within a layer.  
- User requests to change the order of any numbered items in the system.  
- Any operation that requires renaming numbered folders/files to reflect a new ordering.

---

<!-- section_id: "7097da17-0cc7-411b-85ce-cedbba0bcab3" -->
## 1. Pre-Operation: Load Required Context

**Before performing any reordering operation, you MUST load the following context:**

<!-- section_id: "653079b2-1729-461e-80cf-09facae7516c" -->
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

<!-- section_id: "9182ab2e-bb77-41f9-a281-7f9852e3216a" -->
### 1.2 For Stage Reordering

1. **Read the Layer/Stage Framework:**
   - `0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
   - Understand how stages are numbered and organized.

2. **Check Current Stage Structure:**
   - Review the `0.99_stages/` folder in the relevant layer to see current stage numbering.

<!-- section_id: "5e074ce0-9247-44c9-9aea-2b209c9011de" -->
### 1.3 For Other Numbered Item Reordering

1. **Identify the registry/index system** (if any) for the items being reordered.
2. **Load documentation** explaining the numbering scheme and any automation scripts.

---

<!-- section_id: "367ab5a4-fbf1-4d96-aae4-68c3ae8449bf" -->
## 2. Reordering Steps

<!-- section_id: "032b8a4f-7919-46fe-97e4-1a81cbeed413" -->
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

<!-- section_id: "d3d02adc-fb27-448d-9d65-986e658c3d0f" -->
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

<!-- section_id: "4afc560a-b8be-433e-946c-396aee9056f0" -->
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

<!-- section_id: "b41f9a24-b0ea-4640-82df-57a53b7fc857" -->
## 3. Post-Operation: Verification and Documentation

<!-- section_id: "09039656-8e8d-431d-bc30-4b84798a6f72" -->
### 3.1 Verification Checklist

After any reordering operation:

- [ ] All folders/files have been renamed to reflect the new order.
- [ ] Any registries or indices have been regenerated.
- [ ] Alias files (if applicable) still point to the correct locations.
- [ ] Status files (if applicable) have been updated.
- [ ] No broken references exist (check with appropriate tools).

<!-- section_id: "1c01a1fe-5609-4833-9155-51a498f61f22" -->
### 3.2 Documentation Updates

- Update any README files that list the order of items.
- Update any master indices or documentation maps.
- Note any breaking changes in commit messages.

<!-- section_id: "5ed1d29c-25f6-4d7a-897d-c83845ef5e24" -->
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

<!-- section_id: "c19e50ae-3508-42e5-a00e-0ec20e8efe5b" -->
## 4. Common Patterns and Examples

<!-- section_id: "eb7b85a0-a606-4926-a217-abdf14ed2e97" -->
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

<!-- section_id: "92d4c899-0191-4d8c-bb25-8b3573b101b7" -->
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

<!-- section_id: "499b2549-f0d7-4bfb-bdb3-aea85d5ead30" -->
## 5. Error Prevention

<!-- section_id: "dd2855dd-96b8-460e-aa0b-0b31a6d96875" -->
### 5.1 Before Starting

- **Always check current state** by reading the registry/index files.
- **Always use temporary numbers** (0.99, 0.98, etc.) to avoid conflicts.
- **Never skip the registry regeneration step** after reordering.

<!-- section_id: "ba9bf94a-651b-4166-87f9-2cf0c6b439ea" -->
### 5.2 During Operation

- **Work in small steps** - rename one folder at a time and verify.
- **Keep track of what you've moved** - note the old and new numbers.
- **Test as you go** - verify the structure is correct before moving to the next item.

<!-- section_id: "17cf9d68-b688-4b25-baad-35ff4ca202a5" -->
### 5.3 After Operation

- **Always regenerate registries/indices** - this is critical for system integrity.
- **Verify the final state** - check that everything is in the correct order.
- **Check for broken references** - use check scripts if available.

---

<!-- section_id: "faa9989d-066d-4c03-a6a9-fd01a9b35fb4" -->
## 6. Integration with Other Protocols

This protocol works in conjunction with:

- **Protocol Writing Standard:** When documenting reordering operations, follow the protocol writing standard.
- **File Documentation Protocol:** If reordering creates new documentation needs, follow the file documentation protocol.
- **Git Commit Rule:** Always commit and push after successful reordering operations.

---

<!-- section_id: "135034c7-7096-4d2d-9ac2-57822b3813e2" -->
## 7. Troubleshooting

<!-- section_id: "b111faad-733b-424f-9b4f-665dde1a2fd8" -->
### Problem: Registry generation fails
- **Solution:** Check that all folder names follow the expected pattern (e.g., `sub_layer_0_XX_slug`).
- Verify that the registry script can find all sub-layer folders.

<!-- section_id: "c4af0e77-7a97-4d7a-945e-15315b1fcb33" -->
### Problem: Alias files point to wrong locations
- **Solution:** Regenerate the registry - alias files are auto-generated from the registry.

<!-- section_id: "9f5bcb7a-027e-41e5-a3be-bba2224e5344" -->
### Problem: Hard-linked references break
- **Solution:** Update references to use alias paths instead of numeric paths.
- Use the `check-hardlinks` script to find all hard-linked references.

<!-- section_id: "5a9aacde-f7a6-4567-b83a-9366f866e7b3" -->
### Problem: Status files show incorrect current stage
- **Solution:** Manually update status JSON files after stage reordering.
- Verify that the stage numbering in status files matches the actual folder names.

