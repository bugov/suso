from .standard import StandardRule


class RuleRegistry:
    _rules = {}

    def get_rule(self, name):
        klass = self._rules.get(name)

        if not klass:
            raise NotImplementedRule

        return klass

    def add_rule(self, name, klass):
        self._rules[name] = klass


class NotImplementedRule(Exception):
    pass


rule_registry = RuleRegistry()
rule_registry.add_rule('standard', StandardRule)
