# Generated from Gremlin.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GremlinParser import GremlinParser
else:
    from GremlinParser import GremlinParser

# This class defines a complete generic visitor for a parse tree produced by GremlinParser.

class GremlinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GremlinParser#queryList.
    def visitQueryList(self, ctx:GremlinParser.QueryListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#query.
    def visitQuery(self, ctx:GremlinParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#emptyQuery.
    def visitEmptyQuery(self, ctx:GremlinParser.EmptyQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSource.
    def visitTraversalSource(self, ctx:GremlinParser.TraversalSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#transactionPart.
    def visitTransactionPart(self, ctx:GremlinParser.TransactionPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#rootTraversal.
    def visitRootTraversal(self, ctx:GremlinParser.RootTraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod.
    def visitTraversalSourceSelfMethod(self, ctx:GremlinParser.TraversalSourceSelfMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_withBulk.
    def visitTraversalSourceSelfMethod_withBulk(self, ctx:GremlinParser.TraversalSourceSelfMethod_withBulkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_withPath.
    def visitTraversalSourceSelfMethod_withPath(self, ctx:GremlinParser.TraversalSourceSelfMethod_withPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_withSack.
    def visitTraversalSourceSelfMethod_withSack(self, ctx:GremlinParser.TraversalSourceSelfMethod_withSackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_withSideEffect.
    def visitTraversalSourceSelfMethod_withSideEffect(self, ctx:GremlinParser.TraversalSourceSelfMethod_withSideEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_withStrategies.
    def visitTraversalSourceSelfMethod_withStrategies(self, ctx:GremlinParser.TraversalSourceSelfMethod_withStrategiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSelfMethod_with.
    def visitTraversalSourceSelfMethod_with(self, ctx:GremlinParser.TraversalSourceSelfMethod_withContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod.
    def visitTraversalSourceSpawnMethod(self, ctx:GremlinParser.TraversalSourceSpawnMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_addE.
    def visitTraversalSourceSpawnMethod_addE(self, ctx:GremlinParser.TraversalSourceSpawnMethod_addEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_addV.
    def visitTraversalSourceSpawnMethod_addV(self, ctx:GremlinParser.TraversalSourceSpawnMethod_addVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_E.
    def visitTraversalSourceSpawnMethod_E(self, ctx:GremlinParser.TraversalSourceSpawnMethod_EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_V.
    def visitTraversalSourceSpawnMethod_V(self, ctx:GremlinParser.TraversalSourceSpawnMethod_VContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_inject.
    def visitTraversalSourceSpawnMethod_inject(self, ctx:GremlinParser.TraversalSourceSpawnMethod_injectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSourceSpawnMethod_io.
    def visitTraversalSourceSpawnMethod_io(self, ctx:GremlinParser.TraversalSourceSpawnMethod_ioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#chainedTraversal.
    def visitChainedTraversal(self, ctx:GremlinParser.ChainedTraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#chainedParentOfGraphTraversal.
    def visitChainedParentOfGraphTraversal(self, ctx:GremlinParser.ChainedParentOfGraphTraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#nestedTraversal.
    def visitNestedTraversal(self, ctx:GremlinParser.NestedTraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#terminatedTraversal.
    def visitTerminatedTraversal(self, ctx:GremlinParser.TerminatedTraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod.
    def visitTraversalMethod(self, ctx:GremlinParser.TraversalMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_V.
    def visitTraversalMethod_V(self, ctx:GremlinParser.TraversalMethod_VContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_addE_String.
    def visitTraversalMethod_addE_String(self, ctx:GremlinParser.TraversalMethod_addE_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_addE_Traversal.
    def visitTraversalMethod_addE_Traversal(self, ctx:GremlinParser.TraversalMethod_addE_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_addV_Empty.
    def visitTraversalMethod_addV_Empty(self, ctx:GremlinParser.TraversalMethod_addV_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_addV_String.
    def visitTraversalMethod_addV_String(self, ctx:GremlinParser.TraversalMethod_addV_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_addV_Traversal.
    def visitTraversalMethod_addV_Traversal(self, ctx:GremlinParser.TraversalMethod_addV_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_aggregate_Scope_String.
    def visitTraversalMethod_aggregate_Scope_String(self, ctx:GremlinParser.TraversalMethod_aggregate_Scope_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_aggregate_String.
    def visitTraversalMethod_aggregate_String(self, ctx:GremlinParser.TraversalMethod_aggregate_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_and.
    def visitTraversalMethod_and(self, ctx:GremlinParser.TraversalMethod_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_as.
    def visitTraversalMethod_as(self, ctx:GremlinParser.TraversalMethod_asContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_barrier_Consumer.
    def visitTraversalMethod_barrier_Consumer(self, ctx:GremlinParser.TraversalMethod_barrier_ConsumerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_barrier_Empty.
    def visitTraversalMethod_barrier_Empty(self, ctx:GremlinParser.TraversalMethod_barrier_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_barrier_int.
    def visitTraversalMethod_barrier_int(self, ctx:GremlinParser.TraversalMethod_barrier_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_both.
    def visitTraversalMethod_both(self, ctx:GremlinParser.TraversalMethod_bothContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_bothE.
    def visitTraversalMethod_bothE(self, ctx:GremlinParser.TraversalMethod_bothEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_bothV.
    def visitTraversalMethod_bothV(self, ctx:GremlinParser.TraversalMethod_bothVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_branch.
    def visitTraversalMethod_branch(self, ctx:GremlinParser.TraversalMethod_branchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Comparator.
    def visitTraversalMethod_by_Comparator(self, ctx:GremlinParser.TraversalMethod_by_ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Empty.
    def visitTraversalMethod_by_Empty(self, ctx:GremlinParser.TraversalMethod_by_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Function.
    def visitTraversalMethod_by_Function(self, ctx:GremlinParser.TraversalMethod_by_FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Function_Comparator.
    def visitTraversalMethod_by_Function_Comparator(self, ctx:GremlinParser.TraversalMethod_by_Function_ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Order.
    def visitTraversalMethod_by_Order(self, ctx:GremlinParser.TraversalMethod_by_OrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_String.
    def visitTraversalMethod_by_String(self, ctx:GremlinParser.TraversalMethod_by_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_String_Comparator.
    def visitTraversalMethod_by_String_Comparator(self, ctx:GremlinParser.TraversalMethod_by_String_ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_T.
    def visitTraversalMethod_by_T(self, ctx:GremlinParser.TraversalMethod_by_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Traversal.
    def visitTraversalMethod_by_Traversal(self, ctx:GremlinParser.TraversalMethod_by_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_by_Traversal_Comparator.
    def visitTraversalMethod_by_Traversal_Comparator(self, ctx:GremlinParser.TraversalMethod_by_Traversal_ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_cap.
    def visitTraversalMethod_cap(self, ctx:GremlinParser.TraversalMethod_capContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Function.
    def visitTraversalMethod_choose_Function(self, ctx:GremlinParser.TraversalMethod_choose_FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Predicate_Traversal.
    def visitTraversalMethod_choose_Predicate_Traversal(self, ctx:GremlinParser.TraversalMethod_choose_Predicate_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Predicate_Traversal_Traversal.
    def visitTraversalMethod_choose_Predicate_Traversal_Traversal(self, ctx:GremlinParser.TraversalMethod_choose_Predicate_Traversal_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Traversal.
    def visitTraversalMethod_choose_Traversal(self, ctx:GremlinParser.TraversalMethod_choose_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Traversal_Traversal.
    def visitTraversalMethod_choose_Traversal_Traversal(self, ctx:GremlinParser.TraversalMethod_choose_Traversal_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_choose_Traversal_Traversal_Traversal.
    def visitTraversalMethod_choose_Traversal_Traversal_Traversal(self, ctx:GremlinParser.TraversalMethod_choose_Traversal_Traversal_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_coalesce.
    def visitTraversalMethod_coalesce(self, ctx:GremlinParser.TraversalMethod_coalesceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_coin.
    def visitTraversalMethod_coin(self, ctx:GremlinParser.TraversalMethod_coinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_connectedComponent.
    def visitTraversalMethod_connectedComponent(self, ctx:GremlinParser.TraversalMethod_connectedComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_constant.
    def visitTraversalMethod_constant(self, ctx:GremlinParser.TraversalMethod_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_count_Empty.
    def visitTraversalMethod_count_Empty(self, ctx:GremlinParser.TraversalMethod_count_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_count_Scope.
    def visitTraversalMethod_count_Scope(self, ctx:GremlinParser.TraversalMethod_count_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_cyclicPath.
    def visitTraversalMethod_cyclicPath(self, ctx:GremlinParser.TraversalMethod_cyclicPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_dedup_Scope_String.
    def visitTraversalMethod_dedup_Scope_String(self, ctx:GremlinParser.TraversalMethod_dedup_Scope_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_dedup_String.
    def visitTraversalMethod_dedup_String(self, ctx:GremlinParser.TraversalMethod_dedup_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_drop.
    def visitTraversalMethod_drop(self, ctx:GremlinParser.TraversalMethod_dropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_elementMap.
    def visitTraversalMethod_elementMap(self, ctx:GremlinParser.TraversalMethod_elementMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_emit_Empty.
    def visitTraversalMethod_emit_Empty(self, ctx:GremlinParser.TraversalMethod_emit_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_emit_Predicate.
    def visitTraversalMethod_emit_Predicate(self, ctx:GremlinParser.TraversalMethod_emit_PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_emit_Traversal.
    def visitTraversalMethod_emit_Traversal(self, ctx:GremlinParser.TraversalMethod_emit_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_filter_Predicate.
    def visitTraversalMethod_filter_Predicate(self, ctx:GremlinParser.TraversalMethod_filter_PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_filter_Traversal.
    def visitTraversalMethod_filter_Traversal(self, ctx:GremlinParser.TraversalMethod_filter_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_flatMap.
    def visitTraversalMethod_flatMap(self, ctx:GremlinParser.TraversalMethod_flatMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_fold_Empty.
    def visitTraversalMethod_fold_Empty(self, ctx:GremlinParser.TraversalMethod_fold_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_fold_Object_BiFunction.
    def visitTraversalMethod_fold_Object_BiFunction(self, ctx:GremlinParser.TraversalMethod_fold_Object_BiFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_from_String.
    def visitTraversalMethod_from_String(self, ctx:GremlinParser.TraversalMethod_from_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_from_Traversal.
    def visitTraversalMethod_from_Traversal(self, ctx:GremlinParser.TraversalMethod_from_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_group_Empty.
    def visitTraversalMethod_group_Empty(self, ctx:GremlinParser.TraversalMethod_group_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_group_String.
    def visitTraversalMethod_group_String(self, ctx:GremlinParser.TraversalMethod_group_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_groupCount_Empty.
    def visitTraversalMethod_groupCount_Empty(self, ctx:GremlinParser.TraversalMethod_groupCount_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_groupCount_String.
    def visitTraversalMethod_groupCount_String(self, ctx:GremlinParser.TraversalMethod_groupCount_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String.
    def visitTraversalMethod_has_String(self, ctx:GremlinParser.TraversalMethod_has_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String_Object.
    def visitTraversalMethod_has_String_Object(self, ctx:GremlinParser.TraversalMethod_has_String_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String_P.
    def visitTraversalMethod_has_String_P(self, ctx:GremlinParser.TraversalMethod_has_String_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String_String_Object.
    def visitTraversalMethod_has_String_String_Object(self, ctx:GremlinParser.TraversalMethod_has_String_String_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String_String_P.
    def visitTraversalMethod_has_String_String_P(self, ctx:GremlinParser.TraversalMethod_has_String_String_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_String_Traversal.
    def visitTraversalMethod_has_String_Traversal(self, ctx:GremlinParser.TraversalMethod_has_String_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_T_Object.
    def visitTraversalMethod_has_T_Object(self, ctx:GremlinParser.TraversalMethod_has_T_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_T_P.
    def visitTraversalMethod_has_T_P(self, ctx:GremlinParser.TraversalMethod_has_T_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_has_T_Traversal.
    def visitTraversalMethod_has_T_Traversal(self, ctx:GremlinParser.TraversalMethod_has_T_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasId_Object_Object.
    def visitTraversalMethod_hasId_Object_Object(self, ctx:GremlinParser.TraversalMethod_hasId_Object_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasId_P.
    def visitTraversalMethod_hasId_P(self, ctx:GremlinParser.TraversalMethod_hasId_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasKey_P.
    def visitTraversalMethod_hasKey_P(self, ctx:GremlinParser.TraversalMethod_hasKey_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasKey_String_String.
    def visitTraversalMethod_hasKey_String_String(self, ctx:GremlinParser.TraversalMethod_hasKey_String_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasLabel_P.
    def visitTraversalMethod_hasLabel_P(self, ctx:GremlinParser.TraversalMethod_hasLabel_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasLabel_String_String.
    def visitTraversalMethod_hasLabel_String_String(self, ctx:GremlinParser.TraversalMethod_hasLabel_String_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasNot.
    def visitTraversalMethod_hasNot(self, ctx:GremlinParser.TraversalMethod_hasNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasValue_Object_Object.
    def visitTraversalMethod_hasValue_Object_Object(self, ctx:GremlinParser.TraversalMethod_hasValue_Object_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_hasValue_P.
    def visitTraversalMethod_hasValue_P(self, ctx:GremlinParser.TraversalMethod_hasValue_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_id.
    def visitTraversalMethod_id(self, ctx:GremlinParser.TraversalMethod_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_identity.
    def visitTraversalMethod_identity(self, ctx:GremlinParser.TraversalMethod_identityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_in.
    def visitTraversalMethod_in(self, ctx:GremlinParser.TraversalMethod_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_inE.
    def visitTraversalMethod_inE(self, ctx:GremlinParser.TraversalMethod_inEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_inV.
    def visitTraversalMethod_inV(self, ctx:GremlinParser.TraversalMethod_inVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_index.
    def visitTraversalMethod_index(self, ctx:GremlinParser.TraversalMethod_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_inject.
    def visitTraversalMethod_inject(self, ctx:GremlinParser.TraversalMethod_injectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_is_Object.
    def visitTraversalMethod_is_Object(self, ctx:GremlinParser.TraversalMethod_is_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_is_P.
    def visitTraversalMethod_is_P(self, ctx:GremlinParser.TraversalMethod_is_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_key.
    def visitTraversalMethod_key(self, ctx:GremlinParser.TraversalMethod_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_label.
    def visitTraversalMethod_label(self, ctx:GremlinParser.TraversalMethod_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_limit_Scope_long.
    def visitTraversalMethod_limit_Scope_long(self, ctx:GremlinParser.TraversalMethod_limit_Scope_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_limit_long.
    def visitTraversalMethod_limit_long(self, ctx:GremlinParser.TraversalMethod_limit_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_local.
    def visitTraversalMethod_local(self, ctx:GremlinParser.TraversalMethod_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_loops_Empty.
    def visitTraversalMethod_loops_Empty(self, ctx:GremlinParser.TraversalMethod_loops_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_loops_String.
    def visitTraversalMethod_loops_String(self, ctx:GremlinParser.TraversalMethod_loops_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_map.
    def visitTraversalMethod_map(self, ctx:GremlinParser.TraversalMethod_mapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_match.
    def visitTraversalMethod_match(self, ctx:GremlinParser.TraversalMethod_matchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_math.
    def visitTraversalMethod_math(self, ctx:GremlinParser.TraversalMethod_mathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_max_Empty.
    def visitTraversalMethod_max_Empty(self, ctx:GremlinParser.TraversalMethod_max_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_max_Scope.
    def visitTraversalMethod_max_Scope(self, ctx:GremlinParser.TraversalMethod_max_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_mean_Empty.
    def visitTraversalMethod_mean_Empty(self, ctx:GremlinParser.TraversalMethod_mean_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_mean_Scope.
    def visitTraversalMethod_mean_Scope(self, ctx:GremlinParser.TraversalMethod_mean_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_min_Empty.
    def visitTraversalMethod_min_Empty(self, ctx:GremlinParser.TraversalMethod_min_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_min_Scope.
    def visitTraversalMethod_min_Scope(self, ctx:GremlinParser.TraversalMethod_min_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_not.
    def visitTraversalMethod_not(self, ctx:GremlinParser.TraversalMethod_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_option_Predicate_Traversal.
    def visitTraversalMethod_option_Predicate_Traversal(self, ctx:GremlinParser.TraversalMethod_option_Predicate_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_option_Object_Traversal.
    def visitTraversalMethod_option_Object_Traversal(self, ctx:GremlinParser.TraversalMethod_option_Object_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_option_Traversal.
    def visitTraversalMethod_option_Traversal(self, ctx:GremlinParser.TraversalMethod_option_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_optional.
    def visitTraversalMethod_optional(self, ctx:GremlinParser.TraversalMethod_optionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_or.
    def visitTraversalMethod_or(self, ctx:GremlinParser.TraversalMethod_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_order_Empty.
    def visitTraversalMethod_order_Empty(self, ctx:GremlinParser.TraversalMethod_order_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_order_Scope.
    def visitTraversalMethod_order_Scope(self, ctx:GremlinParser.TraversalMethod_order_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_otherV.
    def visitTraversalMethod_otherV(self, ctx:GremlinParser.TraversalMethod_otherVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_out.
    def visitTraversalMethod_out(self, ctx:GremlinParser.TraversalMethod_outContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_outE.
    def visitTraversalMethod_outE(self, ctx:GremlinParser.TraversalMethod_outEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_outV.
    def visitTraversalMethod_outV(self, ctx:GremlinParser.TraversalMethod_outVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_pageRank_Empty.
    def visitTraversalMethod_pageRank_Empty(self, ctx:GremlinParser.TraversalMethod_pageRank_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_pageRank_double.
    def visitTraversalMethod_pageRank_double(self, ctx:GremlinParser.TraversalMethod_pageRank_doubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_path.
    def visitTraversalMethod_path(self, ctx:GremlinParser.TraversalMethod_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_peerPressure.
    def visitTraversalMethod_peerPressure(self, ctx:GremlinParser.TraversalMethod_peerPressureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_profile_Empty.
    def visitTraversalMethod_profile_Empty(self, ctx:GremlinParser.TraversalMethod_profile_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_profile_String.
    def visitTraversalMethod_profile_String(self, ctx:GremlinParser.TraversalMethod_profile_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_project.
    def visitTraversalMethod_project(self, ctx:GremlinParser.TraversalMethod_projectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_properties.
    def visitTraversalMethod_properties(self, ctx:GremlinParser.TraversalMethod_propertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_property_Cardinality_Object_Object_Object.
    def visitTraversalMethod_property_Cardinality_Object_Object_Object(self, ctx:GremlinParser.TraversalMethod_property_Cardinality_Object_Object_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_property_Object_Object_Object.
    def visitTraversalMethod_property_Object_Object_Object(self, ctx:GremlinParser.TraversalMethod_property_Object_Object_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_propertyMap.
    def visitTraversalMethod_propertyMap(self, ctx:GremlinParser.TraversalMethod_propertyMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_range_Scope_long_long.
    def visitTraversalMethod_range_Scope_long_long(self, ctx:GremlinParser.TraversalMethod_range_Scope_long_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_range_long_long.
    def visitTraversalMethod_range_long_long(self, ctx:GremlinParser.TraversalMethod_range_long_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_read.
    def visitTraversalMethod_read(self, ctx:GremlinParser.TraversalMethod_readContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_repeat_String_Traversal.
    def visitTraversalMethod_repeat_String_Traversal(self, ctx:GremlinParser.TraversalMethod_repeat_String_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_repeat_Traversal.
    def visitTraversalMethod_repeat_Traversal(self, ctx:GremlinParser.TraversalMethod_repeat_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sack_BiFunction.
    def visitTraversalMethod_sack_BiFunction(self, ctx:GremlinParser.TraversalMethod_sack_BiFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sack_Empty.
    def visitTraversalMethod_sack_Empty(self, ctx:GremlinParser.TraversalMethod_sack_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sample_Scope_int.
    def visitTraversalMethod_sample_Scope_int(self, ctx:GremlinParser.TraversalMethod_sample_Scope_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sample_int.
    def visitTraversalMethod_sample_int(self, ctx:GremlinParser.TraversalMethod_sample_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_Column.
    def visitTraversalMethod_select_Column(self, ctx:GremlinParser.TraversalMethod_select_ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_Pop_String.
    def visitTraversalMethod_select_Pop_String(self, ctx:GremlinParser.TraversalMethod_select_Pop_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_Pop_String_String_String.
    def visitTraversalMethod_select_Pop_String_String_String(self, ctx:GremlinParser.TraversalMethod_select_Pop_String_String_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_Pop_Traversal.
    def visitTraversalMethod_select_Pop_Traversal(self, ctx:GremlinParser.TraversalMethod_select_Pop_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_String.
    def visitTraversalMethod_select_String(self, ctx:GremlinParser.TraversalMethod_select_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_String_String_String.
    def visitTraversalMethod_select_String_String_String(self, ctx:GremlinParser.TraversalMethod_select_String_String_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_select_Traversal.
    def visitTraversalMethod_select_Traversal(self, ctx:GremlinParser.TraversalMethod_select_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_shortestPath.
    def visitTraversalMethod_shortestPath(self, ctx:GremlinParser.TraversalMethod_shortestPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sideEffect.
    def visitTraversalMethod_sideEffect(self, ctx:GremlinParser.TraversalMethod_sideEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_simplePath.
    def visitTraversalMethod_simplePath(self, ctx:GremlinParser.TraversalMethod_simplePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_skip_Scope_long.
    def visitTraversalMethod_skip_Scope_long(self, ctx:GremlinParser.TraversalMethod_skip_Scope_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_skip_long.
    def visitTraversalMethod_skip_long(self, ctx:GremlinParser.TraversalMethod_skip_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_store.
    def visitTraversalMethod_store(self, ctx:GremlinParser.TraversalMethod_storeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_subgraph.
    def visitTraversalMethod_subgraph(self, ctx:GremlinParser.TraversalMethod_subgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sum_Empty.
    def visitTraversalMethod_sum_Empty(self, ctx:GremlinParser.TraversalMethod_sum_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_sum_Scope.
    def visitTraversalMethod_sum_Scope(self, ctx:GremlinParser.TraversalMethod_sum_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tail_Empty.
    def visitTraversalMethod_tail_Empty(self, ctx:GremlinParser.TraversalMethod_tail_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tail_Scope.
    def visitTraversalMethod_tail_Scope(self, ctx:GremlinParser.TraversalMethod_tail_ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tail_Scope_long.
    def visitTraversalMethod_tail_Scope_long(self, ctx:GremlinParser.TraversalMethod_tail_Scope_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tail_long.
    def visitTraversalMethod_tail_long(self, ctx:GremlinParser.TraversalMethod_tail_longContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_timeLimit.
    def visitTraversalMethod_timeLimit(self, ctx:GremlinParser.TraversalMethod_timeLimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_times.
    def visitTraversalMethod_times(self, ctx:GremlinParser.TraversalMethod_timesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_to_Direction_String.
    def visitTraversalMethod_to_Direction_String(self, ctx:GremlinParser.TraversalMethod_to_Direction_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_to_String.
    def visitTraversalMethod_to_String(self, ctx:GremlinParser.TraversalMethod_to_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_to_Traversal.
    def visitTraversalMethod_to_Traversal(self, ctx:GremlinParser.TraversalMethod_to_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_toE.
    def visitTraversalMethod_toE(self, ctx:GremlinParser.TraversalMethod_toEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_toV.
    def visitTraversalMethod_toV(self, ctx:GremlinParser.TraversalMethod_toVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tree_Empty.
    def visitTraversalMethod_tree_Empty(self, ctx:GremlinParser.TraversalMethod_tree_EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_tree_String.
    def visitTraversalMethod_tree_String(self, ctx:GremlinParser.TraversalMethod_tree_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_unfold.
    def visitTraversalMethod_unfold(self, ctx:GremlinParser.TraversalMethod_unfoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_union.
    def visitTraversalMethod_union(self, ctx:GremlinParser.TraversalMethod_unionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_until_Predicate.
    def visitTraversalMethod_until_Predicate(self, ctx:GremlinParser.TraversalMethod_until_PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_until_Traversal.
    def visitTraversalMethod_until_Traversal(self, ctx:GremlinParser.TraversalMethod_until_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_value.
    def visitTraversalMethod_value(self, ctx:GremlinParser.TraversalMethod_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_valueMap_String.
    def visitTraversalMethod_valueMap_String(self, ctx:GremlinParser.TraversalMethod_valueMap_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_valueMap_boolean_String.
    def visitTraversalMethod_valueMap_boolean_String(self, ctx:GremlinParser.TraversalMethod_valueMap_boolean_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_values.
    def visitTraversalMethod_values(self, ctx:GremlinParser.TraversalMethod_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_where_P.
    def visitTraversalMethod_where_P(self, ctx:GremlinParser.TraversalMethod_where_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_where_String_P.
    def visitTraversalMethod_where_String_P(self, ctx:GremlinParser.TraversalMethod_where_String_PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_where_Traversal.
    def visitTraversalMethod_where_Traversal(self, ctx:GremlinParser.TraversalMethod_where_TraversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_with_String.
    def visitTraversalMethod_with_String(self, ctx:GremlinParser.TraversalMethod_with_StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_with_String_Object.
    def visitTraversalMethod_with_String_Object(self, ctx:GremlinParser.TraversalMethod_with_String_ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalMethod_write.
    def visitTraversalMethod_write(self, ctx:GremlinParser.TraversalMethod_writeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategy.
    def visitTraversalStrategy(self, ctx:GremlinParser.TraversalStrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyArgs_PartitionStrategy.
    def visitTraversalStrategyArgs_PartitionStrategy(self, ctx:GremlinParser.TraversalStrategyArgs_PartitionStrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyArgs_SubgraphStrategy.
    def visitTraversalStrategyArgs_SubgraphStrategy(self, ctx:GremlinParser.TraversalStrategyArgs_SubgraphStrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyArgs_EdgeLabelVerificationStrategy.
    def visitTraversalStrategyArgs_EdgeLabelVerificationStrategy(self, ctx:GremlinParser.TraversalStrategyArgs_EdgeLabelVerificationStrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyArgs_ReservedKeysVerificationStrategy.
    def visitTraversalStrategyArgs_ReservedKeysVerificationStrategy(self, ctx:GremlinParser.TraversalStrategyArgs_ReservedKeysVerificationStrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalScope.
    def visitTraversalScope(self, ctx:GremlinParser.TraversalScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalToken.
    def visitTraversalToken(self, ctx:GremlinParser.TraversalTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalOrder.
    def visitTraversalOrder(self, ctx:GremlinParser.TraversalOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalDirection.
    def visitTraversalDirection(self, ctx:GremlinParser.TraversalDirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalCardinality.
    def visitTraversalCardinality(self, ctx:GremlinParser.TraversalCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalColumn.
    def visitTraversalColumn(self, ctx:GremlinParser.TraversalColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPop.
    def visitTraversalPop(self, ctx:GremlinParser.TraversalPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalOperator.
    def visitTraversalOperator(self, ctx:GremlinParser.TraversalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalOptionParent.
    def visitTraversalOptionParent(self, ctx:GremlinParser.TraversalOptionParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate.
    def visitTraversalPredicate(self, ctx:GremlinParser.TraversalPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod.
    def visitTraversalTerminalMethod(self, ctx:GremlinParser.TraversalTerminalMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSackMethod.
    def visitTraversalSackMethod(self, ctx:GremlinParser.TraversalSackMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSelfMethod.
    def visitTraversalSelfMethod(self, ctx:GremlinParser.TraversalSelfMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalComparator.
    def visitTraversalComparator(self, ctx:GremlinParser.TraversalComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalFunction.
    def visitTraversalFunction(self, ctx:GremlinParser.TraversalFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalBiFunction.
    def visitTraversalBiFunction(self, ctx:GremlinParser.TraversalBiFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_eq.
    def visitTraversalPredicate_eq(self, ctx:GremlinParser.TraversalPredicate_eqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_neq.
    def visitTraversalPredicate_neq(self, ctx:GremlinParser.TraversalPredicate_neqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_lt.
    def visitTraversalPredicate_lt(self, ctx:GremlinParser.TraversalPredicate_ltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_lte.
    def visitTraversalPredicate_lte(self, ctx:GremlinParser.TraversalPredicate_lteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_gt.
    def visitTraversalPredicate_gt(self, ctx:GremlinParser.TraversalPredicate_gtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_gte.
    def visitTraversalPredicate_gte(self, ctx:GremlinParser.TraversalPredicate_gteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_inside.
    def visitTraversalPredicate_inside(self, ctx:GremlinParser.TraversalPredicate_insideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_outside.
    def visitTraversalPredicate_outside(self, ctx:GremlinParser.TraversalPredicate_outsideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_between.
    def visitTraversalPredicate_between(self, ctx:GremlinParser.TraversalPredicate_betweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_within.
    def visitTraversalPredicate_within(self, ctx:GremlinParser.TraversalPredicate_withinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_without.
    def visitTraversalPredicate_without(self, ctx:GremlinParser.TraversalPredicate_withoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_not.
    def visitTraversalPredicate_not(self, ctx:GremlinParser.TraversalPredicate_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_containing.
    def visitTraversalPredicate_containing(self, ctx:GremlinParser.TraversalPredicate_containingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_notContaining.
    def visitTraversalPredicate_notContaining(self, ctx:GremlinParser.TraversalPredicate_notContainingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_startingWith.
    def visitTraversalPredicate_startingWith(self, ctx:GremlinParser.TraversalPredicate_startingWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_notStartingWith.
    def visitTraversalPredicate_notStartingWith(self, ctx:GremlinParser.TraversalPredicate_notStartingWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_endingWith.
    def visitTraversalPredicate_endingWith(self, ctx:GremlinParser.TraversalPredicate_endingWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalPredicate_notEndingWith.
    def visitTraversalPredicate_notEndingWith(self, ctx:GremlinParser.TraversalPredicate_notEndingWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_explain.
    def visitTraversalTerminalMethod_explain(self, ctx:GremlinParser.TraversalTerminalMethod_explainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_hasNext.
    def visitTraversalTerminalMethod_hasNext(self, ctx:GremlinParser.TraversalTerminalMethod_hasNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_iterate.
    def visitTraversalTerminalMethod_iterate(self, ctx:GremlinParser.TraversalTerminalMethod_iterateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_tryNext.
    def visitTraversalTerminalMethod_tryNext(self, ctx:GremlinParser.TraversalTerminalMethod_tryNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_next.
    def visitTraversalTerminalMethod_next(self, ctx:GremlinParser.TraversalTerminalMethod_nextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_toList.
    def visitTraversalTerminalMethod_toList(self, ctx:GremlinParser.TraversalTerminalMethod_toListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_toSet.
    def visitTraversalTerminalMethod_toSet(self, ctx:GremlinParser.TraversalTerminalMethod_toSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalTerminalMethod_toBulkSet.
    def visitTraversalTerminalMethod_toBulkSet(self, ctx:GremlinParser.TraversalTerminalMethod_toBulkSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalSelfMethod_none.
    def visitTraversalSelfMethod_none(self, ctx:GremlinParser.TraversalSelfMethod_noneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants.
    def visitGremlinStringConstants(self, ctx:GremlinParser.GremlinStringConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#pageRankStringConstants.
    def visitPageRankStringConstants(self, ctx:GremlinParser.PageRankStringConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#peerPressureStringConstants.
    def visitPeerPressureStringConstants(self, ctx:GremlinParser.PeerPressureStringConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#shortestPathStringConstants.
    def visitShortestPathStringConstants(self, ctx:GremlinParser.ShortestPathStringConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#withOptionsStringConstants.
    def visitWithOptionsStringConstants(self, ctx:GremlinParser.WithOptionsStringConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_pageRankStringConstants_edges.
    def visitGremlinStringConstants_pageRankStringConstants_edges(self, ctx:GremlinParser.GremlinStringConstants_pageRankStringConstants_edgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_pageRankStringConstants_times.
    def visitGremlinStringConstants_pageRankStringConstants_times(self, ctx:GremlinParser.GremlinStringConstants_pageRankStringConstants_timesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_pageRankStringConstants_propertyName.
    def visitGremlinStringConstants_pageRankStringConstants_propertyName(self, ctx:GremlinParser.GremlinStringConstants_pageRankStringConstants_propertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_peerPressureStringConstants_edges.
    def visitGremlinStringConstants_peerPressureStringConstants_edges(self, ctx:GremlinParser.GremlinStringConstants_peerPressureStringConstants_edgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_peerPressureStringConstants_times.
    def visitGremlinStringConstants_peerPressureStringConstants_times(self, ctx:GremlinParser.GremlinStringConstants_peerPressureStringConstants_timesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_peerPressureStringConstants_propertyName.
    def visitGremlinStringConstants_peerPressureStringConstants_propertyName(self, ctx:GremlinParser.GremlinStringConstants_peerPressureStringConstants_propertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_shortestPathStringConstants_target.
    def visitGremlinStringConstants_shortestPathStringConstants_target(self, ctx:GremlinParser.GremlinStringConstants_shortestPathStringConstants_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_shortestPathStringConstants_edges.
    def visitGremlinStringConstants_shortestPathStringConstants_edges(self, ctx:GremlinParser.GremlinStringConstants_shortestPathStringConstants_edgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_shortestPathStringConstants_distance.
    def visitGremlinStringConstants_shortestPathStringConstants_distance(self, ctx:GremlinParser.GremlinStringConstants_shortestPathStringConstants_distanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_shortestPathStringConstants_maxDistance.
    def visitGremlinStringConstants_shortestPathStringConstants_maxDistance(self, ctx:GremlinParser.GremlinStringConstants_shortestPathStringConstants_maxDistanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_shortestPathStringConstants_includeEdges.
    def visitGremlinStringConstants_shortestPathStringConstants_includeEdges(self, ctx:GremlinParser.GremlinStringConstants_shortestPathStringConstants_includeEdgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_tokens.
    def visitGremlinStringConstants_withOptionsStringConstants_tokens(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_tokensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_none.
    def visitGremlinStringConstants_withOptionsStringConstants_none(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_noneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_ids.
    def visitGremlinStringConstants_withOptionsStringConstants_ids(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_labels.
    def visitGremlinStringConstants_withOptionsStringConstants_labels(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_labelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_keys.
    def visitGremlinStringConstants_withOptionsStringConstants_keys(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_keysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_values.
    def visitGremlinStringConstants_withOptionsStringConstants_values(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_all.
    def visitGremlinStringConstants_withOptionsStringConstants_all(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_allContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_indexer.
    def visitGremlinStringConstants_withOptionsStringConstants_indexer(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_indexerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_list.
    def visitGremlinStringConstants_withOptionsStringConstants_list(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#gremlinStringConstants_withOptionsStringConstants_map.
    def visitGremlinStringConstants_withOptionsStringConstants_map(self, ctx:GremlinParser.GremlinStringConstants_withOptionsStringConstants_mapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#pageRankStringConstant.
    def visitPageRankStringConstant(self, ctx:GremlinParser.PageRankStringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#peerPressureStringConstant.
    def visitPeerPressureStringConstant(self, ctx:GremlinParser.PeerPressureStringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#shortestPathStringConstant.
    def visitShortestPathStringConstant(self, ctx:GremlinParser.ShortestPathStringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#withOptionsStringConstant.
    def visitWithOptionsStringConstant(self, ctx:GremlinParser.WithOptionsStringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyList.
    def visitTraversalStrategyList(self, ctx:GremlinParser.TraversalStrategyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#traversalStrategyExpr.
    def visitTraversalStrategyExpr(self, ctx:GremlinParser.TraversalStrategyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#nestedTraversalList.
    def visitNestedTraversalList(self, ctx:GremlinParser.NestedTraversalListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#nestedTraversalExpr.
    def visitNestedTraversalExpr(self, ctx:GremlinParser.NestedTraversalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteralList.
    def visitGenericLiteralList(self, ctx:GremlinParser.GenericLiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteralExpr.
    def visitGenericLiteralExpr(self, ctx:GremlinParser.GenericLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteralRange.
    def visitGenericLiteralRange(self, ctx:GremlinParser.GenericLiteralRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteralCollection.
    def visitGenericLiteralCollection(self, ctx:GremlinParser.GenericLiteralCollectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#stringLiteralList.
    def visitStringLiteralList(self, ctx:GremlinParser.StringLiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#stringLiteralExpr.
    def visitStringLiteralExpr(self, ctx:GremlinParser.StringLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteral.
    def visitGenericLiteral(self, ctx:GremlinParser.GenericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#genericLiteralMap.
    def visitGenericLiteralMap(self, ctx:GremlinParser.GenericLiteralMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:GremlinParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#floatLiteral.
    def visitFloatLiteral(self, ctx:GremlinParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:GremlinParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#stringLiteral.
    def visitStringLiteral(self, ctx:GremlinParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#dateLiteral.
    def visitDateLiteral(self, ctx:GremlinParser.DateLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GremlinParser#nullLiteral.
    def visitNullLiteral(self, ctx:GremlinParser.NullLiteralContext):
        return self.visitChildren(ctx)



del GremlinParser