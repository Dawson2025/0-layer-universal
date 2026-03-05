---
resource_id: "31b6adb3-adbb-410a-8031-44ca67596336"
resource_type: "document"
resource_name: "interface_definitions"
---
# Interface Definitions

**Purpose**: Contracts between Layer Agents. Each interface defines what a layer PROVIDES to layers above it.
**Design principle**: Interface Segregation (ISP) — small, focused interfaces. Agents depend only on what they use.

---

## IStorageProvider (L2 → L3, L4, L5, L6, L7, L8)

Unified local/cloud storage interface.

```
+ save(data) → Result
+ load(id) → Data
+ delete(id) → Result
+ query(filter) → List[Data]
```

**Provided by**: L2 InfrastructureAgent (via L2.4 Storage Manager)

---

## IAuthProvider (L2 → L3)

Authentication and authorization.

```
+ login(credentials) → User
+ logout() → void
+ check_auth() → bool
+ get_current_user() → User
```

**Provided by**: L2 InfrastructureAgent (via L2.5 Auth System)

---

## IUserProvider (L3 → L4, L8)

User identity and profile access.

```
+ get_user(id) → User
+ get_profile(user_id) → Profile
+ get_session() → Session
```

**Provided by**: L3 UsersAgent

---

## IPhonemeProvider (L4 → L5)

Core phoneme data access.

```
+ get_phoneme(id) → Phoneme
+ list_by_group(group) → List[Phoneme]
+ list_by_type(type) → List[Phoneme]
+ get_all() → List[Phoneme]
```

**Provided by**: L4 PhonemeSystemAgent (via L4.1-L4.3)

---

## IPhonemeAudio (L4 → L6)

Audio generation for individual phonemes.

```
+ get_audio(phoneme_id) → AudioData
+ generate_tts(ipa_symbol) → AudioData
```

**Provided by**: L4 PhonemeSystemAgent (via L4.6 TTS for Phonemes)

---

## IFrequencyProvider (L4 → internal)

Phoneme usage statistics.

```
+ get_frequency(phoneme_id) → float
+ get_top_phonemes(n) → List[Phoneme]
```

**Provided by**: L4 PhonemeSystemAgent (via L4.4 Frequency Tracking)
**Note**: Primarily internal to L4, but available to any requesting agent.

---

## IPhonemeAdmin (L4 → internal)

CRUD operations for phoneme management.

```
+ create_phoneme(data) → Phoneme
+ update_phoneme(id, data) → Phoneme
+ delete_phoneme(id) → Result
+ create_group(data) → Group
```

**Provided by**: L4 PhonemeSystemAgent (via L4.7 Phoneme Admin)
**Note**: Admin interface, typically used by admin users or the Manager Agent.

---

## ITemplateProvider (L5 → L6)

Template and phoneme subset access.

```
+ get_template(id) → Template
+ get_available_phonemes(template_id) → List[Phoneme]
+ apply_to_project(template_id, project_id) → Result
```

**Provided by**: L5 TemplatesAgent

---

## IContentProvider (L6 → L7)

Language content (words, syllables) access.

```
+ get_word(id) → Word
+ create_word(data) → Word
+ get_syllables(word_id) → List[Syllable]
+ get_suggestions(template_id) → List[WordSuggestion]
```

**Provided by**: L6 LanguageContentAgent

---

## IContentAudio (L6 → external)

Audio generation for words and syllables.

```
+ get_word_audio(word_id) → AudioData
+ get_syllable_audio(syllable_id) → AudioData
```

**Provided by**: L6 LanguageContentAgent (via L6.5 TTS for Content)

---

## IProjectProvider (L7 → L8)

Project access and management.

```
+ get_project(id) → Project
+ list_projects(user_id) → List[Project]
+ get_dashboard(user_id) → DashboardData
```

**Provided by**: L7 ProjectsAgent

---

## ICollaborationProvider (L8 → external)

Team collaboration and sharing.

```
+ get_team(id) → Team
+ invite_member(team_id, user_id) → Invite
+ share_project(team_id, project_id) → Result
```

**Provided by**: L8 TeamsAgent

---

## Interface Dependency Map

```
L2 provides: IStorageProvider, IAuthProvider
     ↓
L3 uses: IStorageProvider, IAuthProvider
L3 provides: IUserProvider
     ↓
L4 uses: IUserProvider
L4 provides: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin
     ↓
L5 uses: IPhonemeProvider
L5 provides: ITemplateProvider
     ↓
L6 uses: ITemplateProvider, IPhonemeAudio
L6 provides: IContentProvider, IContentAudio
     ↓
L7 uses: IContentProvider
L7 provides: IProjectProvider
     ↓
L8 uses: IProjectProvider, IUserProvider (skip-link to L3)
L8 provides: ICollaborationProvider
```

## Summary

| Interface | Methods | Provider | Primary Consumer |
|-----------|---------|----------|-----------------|
| IStorageProvider | 4 | L2 | L3 (and all via DB) |
| IAuthProvider | 4 | L2 | L3 |
| IUserProvider | 3 | L3 | L4, L8 |
| IPhonemeProvider | 4 | L4 | L5 |
| IPhonemeAudio | 2 | L4 | L6 |
| IFrequencyProvider | 2 | L4 | Internal |
| IPhonemeAdmin | 4 | L4 | Admin/Manager |
| ITemplateProvider | 3 | L5 | L6 |
| IContentProvider | 4 | L6 | L7 |
| IContentAudio | 2 | L6 | External |
| IProjectProvider | 3 | L7 | L8 |
| ICollaborationProvider | 3 | L8 | External |

**Total**: 12 interfaces, 38 methods
