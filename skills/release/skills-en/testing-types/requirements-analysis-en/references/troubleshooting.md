## Troubleshooting

### Issue 1: Unclear Requirements

**Symptoms:** Requirements are ambiguous, incomplete, or contradictory

**Solution:**
1. List unclear points with specific questions:
   - What is the expected behavior when...?
   - What are the valid input ranges?
   - What should happen in error cases?
2. Communicate with product manager/stakeholders
3. Document clarification results
4. Update requirement documents
5. Get written confirmation of changes

**Prevention:**
- Use structured requirement templates
- Include acceptance criteria
- Add concrete examples
- Define edge cases explicitly

### Issue 2: Missing Test Points

**Symptoms:** Test coverage is incomplete, important scenarios overlooked

**Solution:**
Use comprehensive checklist:
- [ ] Normal scenarios (happy path)
- [ ] Exception scenarios (error handling)
- [ ] Boundary values (min/max/edge cases)
- [ ] Permission validation (role-based access)
- [ ] Data validation (format, type, range)
- [ ] Performance requirements (response time, throughput)
- [ ] Security requirements (authentication, authorization, encryption)
- [ ] Compatibility (browsers, devices, OS)
- [ ] Usability (accessibility, user experience)
- [ ] Integration points (APIs, external services)

**Techniques:**
- Mind mapping for visual coverage
- Traceability matrix (requirements → test points)
- Peer review of analysis
- Use test design techniques systematically

### Issue 3: Conflicting Requirements

**Symptoms:** Requirements contradict each other or are mutually exclusive

**Solution:**
1. Document all conflicts clearly
2. Analyze impact of each option
3. Present trade-offs to stakeholders
4. Facilitate decision-making meeting
5. Update requirements with final decision
6. Communicate changes to all parties

### Issue 4: Non-Functional Requirements Overlooked

**Symptoms:** Only functional requirements analyzed, missing performance/security/usability

**Solution:**
1. Use NFR checklist:
   - Performance (response time, throughput, scalability)
   - Security (authentication, authorization, data protection)
   - Usability (accessibility, user experience, learnability)
   - Reliability (availability, fault tolerance, recovery)
   - Maintainability (code quality, documentation, testability)
   - Compatibility (browsers, devices, platforms)
2. Ask specific NFR questions for each feature
3. Define measurable NFR criteria
4. Include NFR in test planning

### Issue 5: Inadequate Stakeholder Input

**Symptoms:** Analysis based on assumptions, lacking validation from stakeholders

**Solution:**
1. Schedule requirements review sessions
2. Prepare specific questions and scenarios
3. Use prototypes or mockups for validation
4. Document stakeholder feedback
5. Iterate analysis based on input
6. Get sign-off on final analysis

### Issue 6: Analysis Paralysis

**Symptoms:** Spending too much time on analysis, delaying testing

**Solution:**
1. Set time limits for analysis phase
2. Focus on high-priority requirements first
3. Use iterative approach (analyze → test → refine)
4. Accept that some details will emerge during testing
5. Document assumptions and move forward
6. Schedule follow-up reviews

### Get More Help

If the issue persists:
1. Check [FAQ.md](local/FAQ.md)
2. Review example templates in examples/ directory
3. Search [GitHub Issues](https://github.com/naodeng/awesome-qa-skills/issues)
4. Submit a new Issue with detailed information

**Related skills:** test-case-writing-en, test-strategy-en, functional-testing-en.
